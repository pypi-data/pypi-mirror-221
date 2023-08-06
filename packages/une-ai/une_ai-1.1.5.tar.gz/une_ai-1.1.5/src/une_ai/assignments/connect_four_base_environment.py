import random
import numpy as np
from scipy.signal import convolve2d, convolve

from une_ai.models import GameEnvironment
from une_ai.models import GridMap

class InvalidMoveException(Exception):
    pass

class ConnectFourBaseEnvironment(GameEnvironment):

    POWERUPS = ['anvil', 'wall', 'x2']
    N_COLS = 7
    N_ROWS = 6

    def __init__(self):
        super().__init__("Connect Four Game Environment")
        self._game_board = GridMap(ConnectFourBaseEnvironment.N_COLS, ConnectFourBaseEnvironment.N_ROWS, None)
        self._played_powerup = (None, None)
        self._player_turn = 'Y' # yellow always start
    
    def add_player(self, player):
        assert len(self._players) < 2, "It is not possible to add more than 2 players for this game."

        if len(self._players) == 0:
            colour = 'Y'
        else:
            colour = 'R'

        powerup = random.choice(ConnectFourBaseEnvironment.POWERUPS)
        
        self._players[colour] = (player, powerup) # adding player
        return colour
    
    def get_game_state(self):
        game_state = {
            'game-board': self._game_board.copy(),
            'power-up-Y': None if 'Y' not in self._players.keys() else self._players['Y'][1],
            'power-up-R': None if 'R' not in self._players.keys() else self._players['R'][1],
            'player-turn': self._player_turn
        }

        return game_state
    
    def turn(game_state):
        return game_state['player-turn']
    
    def get_openings(game_board, player_colour):
        opponent_colour = 'R' if player_colour == 'Y' else 'Y'
        
        # 7 comes from 2*(n_to_connect - 1) + 1
        kernel = np.array([ 1, 1, 1, 1])
        max_diagonals = game_board.get_width() + game_board.get_height() - 7
        diagonal_idx = lambda normalised_idx: normalised_idx - int(max_diagonals / 2) + 1
        
        game_board_map = game_board.get_map()
        rows = {
            'horizontals': [r for r in game_board_map],
            'verticals': [game_board_map[:, i] for i in range(game_board.get_width())],
            'left-diagonals': [np.diagonal(game_board_map, diagonal_idx(i)) for i in range(max_diagonals)],
            'right-diagonals': [np.diagonal(np.fliplr(game_board_map), diagonal_idx(i)) for i in range(max_diagonals)]
        }

        def fill(row):
            flipped = np.flip(row)
            mode = False
            filled = flipped.copy()
            for i, item in enumerate(flipped):
                if item == player_colour:
                    mode = True
                elif item == opponent_colour:
                    mode = False
                
                if mode == True and item is None:
                    filled[i] = player_colour
            
            return np.flip(filled)

        results = {}
        for k, v in rows.items():
            results[k] = []
            for i, row in enumerate(v):
                row_optimal = fill(row)
                if k == 'horizontals':
                    row_optimal = fill(np.flip(row_optimal))
                
                values = convolve(row == player_colour, kernel, mode="valid")
                values_optimal = convolve(row_optimal == player_colour, kernel, mode="valid")
                
                is_free = True if 4 in values_optimal else False
                if is_free:
                    max_val = np.max(values)
                    if max_val > 0:
                        if k == 'horizontals':
                            idx = ConnectFourBaseEnvironment.N_ROWS - 1 - i
                            results[k].append((idx , max_val))
                        else:
                            results[k].append((i, max_val))

        return results
    
    def get_winner(game_state):
        game_board = game_state['game-board']

        horizontal_kernel = np.array([[ 1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag_kernel = np.eye(4, dtype=np.uint8)
        flipped_diag_kernel = np.fliplr(diag_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diag_kernel, flipped_diag_kernel]

        winners = []
        for player in ['Y', 'R']:
            player_checkers = game_board.get_map() == player
            for kernel in detection_kernels:
                convolved_values = convolve2d(player_checkers, kernel, mode="valid")
                if (convolved_values == 4).any():
                    if player not in winners:
                        winners.append(player)
        
        if len(winners) == 2:
            # both players got 4 connected because of a popup move
            # wins the player of the current turn
            return game_state['player-turn']
        elif len(winners) == 1:
            return winners[0]
        else:
            return None
    
    def get_percepts(self):
        game_state = self.get_game_state()
        return {
            'game-board-sensor': game_state['game-board'],
            'powerups-sensor': {
                'Y': game_state['power-up-Y'],
                'R': game_state['power-up-R'],
            },
            'turn-taking-indicator': self._player_turn
        }
    
    def get_first_free_row(game_board, column_num):
        column = game_board.get_column(column_num)
        for i in range(len(column)-1, -1, -1):
            if column[i] is None:
                return i
        
        return None
    
    def is_valid_column(game_board, col_num):
        return col_num is not None and col_num >= 0 and col_num < game_board.get_width()
    
    def is_column_full(game_board, col_num):
        return ConnectFourBaseEnvironment.get_first_free_row(game_board, col_num) == None
    
    def _change_player_turn(self):
        self._prev_turn = self._player_turn
        if self._player_turn == 'Y':
            self._player_turn = 'R'
        else:
            self._player_turn = 'Y'
    
    def _use_powerup(self, player_colour):
        powerup = self._players[player_colour][1]
        self._players[player_colour][1] = None
        self._played_powerup = (player_colour, powerup)
    
    def transition_result(game_state, action):
        assert action.startswith('use-power-up-') or action.startswith('release-') or action.startswith('popup-'), "Invalid action '{0}'.".format(action)
        try:
            index = int(action.split('-')[-1])
        except:
            index = None
        game_board = game_state['game-board'].copy()
        assert index is not None and index >= 0 and index < game_board.get_width(), "The column index {0} from the action {1} is not a valid index.".format(index, action)

        def release_token(game_board, column_num, checker):
            row = ConnectFourBaseEnvironment.get_first_free_row(game_board, column_num)
            game_board.set_item_value(column_num, row, checker)

        new_game_state = {
            'game-board': game_board,
            'power-up-Y': game_state['power-up-Y'],
            'power-up-R': game_state['power-up-R'],
            'player-turn': game_state['player-turn']
        }

        colour_turn = game_state['player-turn']
        if action.startswith('use-power-up-'):
            # playing turn with a power up
            powerup = game_state['power-up-{0}'.format(colour_turn)]
            if powerup is None:
                raise InvalidMoveException("The player of colour '{0}' does not have a power-up available.".format(colour_turn))
            if powerup not in ConnectFourBaseEnvironment.POWERUPS:
                raise InvalidMoveException("The power-up '{0}' is not a valid power-up value.".format(powerup))
            if not ConnectFourBaseEnvironment.is_valid_column(game_board, index):
                raise InvalidMoveException("Invalid column index {0}. When playing the {1} power up, the agent must use the 'checker-releaser' actuator to select a valid column where to play the power up.".format(index, powerup))
            if ConnectFourBaseEnvironment.is_column_full(game_board, index) and powerup != 'anvil':
                raise InvalidMoveException("The column at index {0} is full".format(index))
            
            # remove powerup because used
            new_game_state['power-up-{0}'.format(colour_turn)] = None

            if powerup == 'anvil':
                for i in range(0, game_board.get_height()):
                    game_board.set_item_value(index, i, None)
                release_token(game_board, index, colour_turn)
                new_game_state['player-turn'] = 'Y' if colour_turn == 'R' else 'R'
                return new_game_state
            elif powerup == 'wall':
                release_token(game_board, index, 'W')
                new_game_state['player-turn'] = 'Y' if colour_turn == 'R' else 'R'
                return new_game_state
            elif powerup == 'x2':
                release_token(game_board, index, colour_turn)
                return new_game_state
        elif action.startswith('popup-'):
            # player decided to popup a checker
            if not ConnectFourBaseEnvironment.is_valid_column(game_board, index):
                raise InvalidMoveException("Invalid column index {0}. When popping out a checker, the actuator 'checker-grabber' must select a valid column index from where to popup the checker.".format(index))
            bottom_idx = game_board.get_height()-1
            bottom_checker = game_board.get_item_value(index, bottom_idx)
            if bottom_checker is None:
                raise InvalidMoveException("The column at index {0} is empty. It is not possible to pop-out checkers from there.".format(index))
            if bottom_checker != colour_turn:
                raise InvalidMoveException("A player can pop-out only their checkers from the bottom of the column. The bottom checker at column index {0} is {1}, whereas the player colour is {2}.".format(index, bottom_checker, colour_turn))
            
            for i in range(bottom_idx, 0, -1):
                top_checker = game_board.get_item_value(index, i-1)
                game_board.set_item_value(index, i, top_checker)
            game_board.set_item_value(index, 0, None)
            new_game_state['player-turn'] = 'Y' if colour_turn == 'R' else 'R'
            return new_game_state
        elif action.startswith('release-'):
            # player decided to add a checker
            if not ConnectFourBaseEnvironment.is_valid_column(game_board, index):
                raise InvalidMoveException("Invalid column index {0}. When releasing a checker, the actuator 'checker-releaser' must select a valid column index where to release the checker.".format(index))
            if ConnectFourBaseEnvironment.is_column_full(game_board, index):
                raise InvalidMoveException("The column at index {0} is full".format(index))
            
            release_token(game_board, index, colour_turn)
            new_game_state['player-turn'] = 'Y' if colour_turn == 'R' else 'R'
            return new_game_state
        
        return new_game_state
    
    def state_transition(self, agent_actuators):
        assert 'checker-handler' not in agent_actuators.keys() or (isinstance(agent_actuators['checker-handler'], tuple) and len(agent_actuators['checker-handler']) == 2), "The actuator 'checker-handler' takes a tuple (handling_type, column_index) as value."

        if 'checker-handler' not in agent_actuators.keys():
            # no transition possible
            return
        
        powerup = agent_actuators['powerup-selector']
        handling_type, column_num = agent_actuators['checker-handler']
        if handling_type not in ['release', 'popup']:
            raise InvalidMoveException("The first value of the tuple in the actuator 'checker-handler' must be either 'release' or 'popup'.")
        
        if powerup == True and handling_type != 'release':
            raise InvalidMoveException("When playing a power up with the 'powerup-selector' actuator set to True, the agent must also use the 'checker-handler' actuator to select a valid column where to release the power up. Instead, the handling type for the 'checker-handler' was set to '{0}'.".format(handling_type))

        action = None
        if powerup == True:
            action = 'use-power-up-{0}'.format(column_num)
        elif handling_type == 'release':
            action = 'release-{0}'.format(column_num)
        elif handling_type == 'popup':
            action = 'popup-{0}'.format(column_num)

        new_state = ConnectFourBaseEnvironment.transition_result(self.get_game_state(), action)

        self._game_board = new_state['game-board'].copy()
        self._players['Y'] = (self._players['Y'][0], new_state['power-up-Y'])
        self._players['R'] = (self._players['Y'][0], new_state['power-up-R'])
        self._player_turn = new_state['player-turn']