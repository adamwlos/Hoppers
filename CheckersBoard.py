class Checkers:

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
        pass

    def other_player(self, player):
        """
        Return the other player
        """
        if(player == self.player_1):
            return self.player_2
        return self.player_1

    def get(self):
        pass

    def valid_coordinate(self, row, col):
        pass

    def jump(self, row, col, drow, dcol):
        pass

    def move(self, row, col):
        pass

    def get_count(self):
        pass


