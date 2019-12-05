class CheckersBoard:

    both = "B"
    empty = " "
    player_1 = "X"
    player_2 = "O"
    #
    def __init__(self):
        """
        Contains properties of CheckersBoard including dimensions, player
        piece types, and board
        
        """
        self.dimension = 10
        self.player_1 = "X"
        self.player_2 = "O"
        self.player_1_king = "KX"
        self.player_2_king = "KO"
        self.empty = " "
        self.both = "B"
        self.turn = self.player_1 
        self.board = [[],[],[],[],[],[],[],[],[],[]]
        # initiate the game board with all of player_1 and player_2 pieces
        # add player 1 pieces to player 1 side of the board            
        for i in range(4):
             for j in range(10):
                # add player 1 peices to each row i on alternating spaces
                if(i%2 == 0 and j%2 != 0):
                    self.board[i].append(self.player_1)
                elif(i%2 == 0 and j%2 == 0):
                    self.board[i].append(self.empty)

                if(i%2 != 0 and j%2 == 0):
                    self.board[i].append(self.player_1)
                elif(i%2 != 0 and j%2 != 0):
                    self.board[i].append(self.empty)

        # add player 2 pieces to player 2 side of the board                     
        for k in range(6,10):
            for p in range(10):
                # add player 2 peices to each row k on alternating spaces
                if(k%2 == 0 and p%2 != 0):
                    self.board[k].append(self.player_2)
                elif(k%2 == 0 and p%2 == 0):
                    self.board[k].append(self.empty)

                if(k%2 != 0 and p%2 == 0):
                    self.board[k].append(self.player_2)
                elif(k%2 != 0 and p%2 != 0):
                    self.board[k].append(self.empty)
       
        # fill the remaining rows with empty spaces
        for m in range(4,6):
            for p in range(10):
                self.board[m].append(self.empty)
                            
                    
    def __str__(self):
        '''
        Return the string representation of the game board
        '''
        current_board = ''
        # loop through positions on the board adding the value at each 
        # position to the string representation
        for row in self.board:
            current_board += "|"
            for position in row:
                current_board += str(position)
                current_board += "|"
            current_board += "\n"
        return current_board


    def other_player(self, player):
        """
        Return the other player
        """
        if(player == self.player_1):
            return self.player_2
        if(player == self.player_2):
            return self.player_1
        if(player == self.player_1_king):
            return self.player_2
        if(player == self.player_2_king):
            return self.player_1
        return self.empty

    def get(self, row, col):
        """
        Return the value at the position row, col on the
        game board. Return -1 if coordinates are invalid.
        """
        if(self.valid_coordinate(row, col) == True):
            return self.board[row][col]
        return -1

    def valid_coordinate(self, row, col):
        """
        Ruturn true iff row, col is a valid coordinate
        """
        if(0 <= row and row <= self.dimension - 1):
            if(0 <= col and col <= self.dimension - 1):
                return True
        return False

    def jump(self, row, col, drow, dcol):
        '''
        Modify the board if piece at row, col can make a move in 
        drow, dcol
        Return True if modification is made, otherwise return False
        '''
        moves_available = 0
        piece = self.get(row, col)
        if abs(drow + dcol) == 1:
            return False

        if(piece == self.empty):
            return False
    
        # check if piece has move and modify the board if it does
        if(not self.has_move(row, col, drow, dcol)):
            return False

        else:

            if(self.get(row + drow, col + dcol) == self.empty):
                piece = self.get(row, col)
                self.board[row][col] = self.empty
                self.board[row + drow][col + dcol] = piece
                self.king_piece(row + drow, col + dcol)

                self.turn = self.other_player(piece)

                return True
            else:
                piece = self.get(row, col)
                self.board[row][col] = self.empty
                self.board[row + drow][col + dcol] = self.empty
                self.board[row + 2*drow][col + 2*dcol] = piece
                self.king_piece(row + 2*drow, col + 2*dcol)
                # change turn to other players turn if player has no more moves if its a regular piece
                if(piece == self.player_1 or piece == self.player_2):
                    # for each direction check if player can take over the opponents piece
                    if(self.has_move(row + 2*drow, col + 2*dcol, drow, dcol) == True):
                        if(self.get(row + 2*drow, col + 2*dcol) == self.other_player(piece)):
                            moves_available += 1

                    if(self.has_move(row + 2*drow, col + 2*dcol, drow, (-1)*dcol) == True):
                        if(self.get(row + 2*drow + drow, col + 2*dcol + (-1)*dcol) == self.other_player(piece)):
                            moves_available += 1

                # change turn to other players turn if player has no more moves if its a king piece    
                elif piece != self.empty:
                    if(self.has_move(row + 2*drow, col + 2*dcol, drow, dcol) == True):
                        if(self.get(row + 2*drow + drow, col + 2*dcol + dcol) == self.other_player(piece)):
                            moves_available += 1

                    if(self.has_move(row + 2*drow, col + 2*dcol, drow, (-1)*dcol) == True):
                        if(self.get(row + 2*drow + drow, col + 2*dcol + (-1)*dcol) == self.other_player(piece)):
                            moves_available += 1

                    if(self.has_move(row + 2*drow, col + 2*dcol, (-1)*drow, dcol) == True):
                        if(self.get(row + 2*drow + (-1)*drow, col + 2*dcol + dcol) == self.other_player(piece)):
                            moves_available += 1

                    if(self.has_move(row + 2*drow, col + 2*dcol, (-1)*drow, (-1)*dcol) == True):
                        if(self.get(row + 2*drow + (-1)*drow, col + 2*dcol + (-1)*dcol) == self.other_player(piece)):
                            moves_available += 1

                if(moves_available == 0):
                    self.turn = self.other_player(piece)

                return True




    def has_move(self, row, col, drow, dcol):
        """
        Return True if piece at position row, col has a
        move in direction drow, dcol
        """
        # check if row and col are valid coordinates
        if(self.valid_coordinate(row, col) == False):
            return False

        # check if row, col has piece on it
        if(self.get(row, col) == self.empty):
            return False
        else:
            piece = self.get(row, col)
            player_other = self.other_player(piece)
            player = self.other_player(player_other)

        # check if it is player's turn
        if(player != self.turn):
            return False

        # check if direction drow, dcol are valid
        if(-1 != drow and drow != 1 and -1 != dcol and dcol != 1):
            return False

        # check if directions are valid for regular pieces
        if(piece == self.player_1):
            if(drow != 1 and (dcol != -1 or dcol != 1)):
                return False
        
        if(piece == self.player_2):
            if(drow != -1 and (dcol != -1 or dcol != 1)):
                return False
        
        # check if player has a valid move in direction drow, dcol
        if(self.get(row + drow, col + dcol) == player_other):
            if(self.get(row + 2*drow, col + 2*dcol) == self.empty):
                return True
        elif(self.get(row + drow, col + dcol) == self.empty):
            return True
        else:
            return False

        
    def has_overtake(self, row, col, drow, dcol):
        """
        Return True if piece at row col has a move in direction drow dcol
        only if it can take an opponents piece
        """
        piece = self.get(row, col)
        other_piece = self.other_player(piece)
        if(self.has_move(row, col, drow, dcol) == True):
            if(self.get(row + drow, col + dcol) == other_piece):
                if(self.get(row + 2*drow, col + 2*dcol) == self.empty):
                    return True
        else: 
            return False

        

    def who_has_move(self):
        p1 = 0
        p2 = 0
        for row in range(10):
            for col in range(10):
                for drow in range(-1, 2):
                    for dcol in range(-1,2):
                        # if self.has_move(row, col, drow, dcol, self.player_1):
                        if self.has_move(row, col, drow, dcol):
                            p1 +=1
                        # elif self.has_move(row, col, drow, dcol, self.player_2):

                        elif self.has_move(row, col, drow, dcol):
                            p2 +=1
        if p1 == 0 and p2 == 0:
            return CheckersBoard.empty
        elif p1 > 0 and p2 > 0:
            return CheckersBoard.both
        elif p1 == 0 and p2 > 0:
            return self.player_2
        else:
            return self.player_1


    def get_count(self, player):
        """
        Return the number of pieces that player has left on
        the board
        """
        count = 0
        # cycle through all the positions on the board, and keep
        # track of how many of player's pieces are on the board
        for row in self.board:
            for position in row:
                if(position == player):
                    count+=1

        return count

    def king_piece(self, row, col):
        """
        If a piece is on the opposite last row change it to a king piece
        Return true if piece is changed to king
        """
        if(self.valid_coordinate(row, col) == False):
            return False
        piece = self.get(row, col)
        # if player 1 piece is at last row on opposite side of board, king it
        if(piece == self.player_1):
            if(row == 9):
                self.board[row][col] = self.player_1_king
                return True
        # if player 2 piece is at last row on opposite side of board, king it
        if(piece == self.player_2):
            if(row == 0):
                self.board[row][col] = self.player_2_king
                return True
        return False