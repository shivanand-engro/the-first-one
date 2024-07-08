document.addEventListener('DOMContentLoaded', (event) => {
    const cells = document.querySelectorAll('.cell');
    const botFirstToggle = document.getElementById('botFirst');
    let currentPlayer = 'x';
    let isGameOver = false

    const assignRandomO = (emptyCells) => {
 
        if (emptyCells.length === 0) {
          console.log('No empty cells available');
          return;
        }
    
        // Select a random empty cell
        const randomIndex = Math.floor(Math.random() * emptyCells.length);
        const randomCell = emptyCells[randomIndex];
    
        // Assign 'O' to the random empty cell
        randomCell.classList.add('o');
        randomCell.textContent = 'O';
      };
    

    const checkWinner = () => {
      const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
      ];
  
      return winPatterns.some(pattern => {
        return pattern.every(index => {
          return cells[index].classList.contains(currentPlayer);
        });
      });
    };
  
    const handleClick = (e) => {
      const cell = e.target;
    
      if (!cell.classList.contains('x') && !cell.classList.contains('o')) {// Log current player
        cell.classList.add(currentPlayer); // Add the class
        cell.textContent = currentPlayer.toUpperCase();
        if (checkWinner()) {
          setTimeout(() => {
            alert(`${currentPlayer.toUpperCase()} wins!`);
            resetBoard();
          }, 100);
        } else if ([...cells].every(cell => cell.classList.contains('x') || cell.classList.contains('o'))) {
          setTimeout(() => {
            alert('Draw!');
            resetBoard();
          }, 100);
        } else {
                currentPlayer = 'o'
            const emptyCells = Array.from(cells).filter(cell => 
                !cell.classList.contains('x') && !cell.classList.contains('o')
              );
              //code for winning
              emptyCells.forEach(cell => {
                if(!isGameOver){
                cell.classList.add('o');
                console.log("checking")
                if(checkWinner()) {
                    cell.textContent = 'O';
                    isGameOver = true;
                    console.log("bot wins");
                    setTimeout(() => {
                        alert(`${'o'.toUpperCase()} wins!`);
                        resetBoard();
                      }, 100);
                } else {
                    cell.classList.remove('o');
                }}
              });
              //code for blocking
              currentPlayer = 'x'
              let isblocked = false
              if(!isGameOver){
              emptyCells.forEach(cell => {
                if(!isblocked){
                cell.classList.add('x');
                if(checkWinner()) {
                    cell.classList.remove('x')
                    cell.classList.add('o')
                    cell.textContent = 'O';
                    isblocked = true;
                    console.log("blocked");
                } else {
                    cell.classList.remove('x');
                }}
              });
              //code for random move
              if(!isblocked){
              console.log("randomized")
              assignRandomO(emptyCells)
              }
            }

        }
      }
    };
    
    cells.forEach(cell => {
      cell.addEventListener('click', handleClick);
    });
    
  
    const resetBoard = () => {
      cells.forEach(cell => {
        cell.classList.remove('x', 'o');
        cell.textContent =""
      });
      currentPlayer = 'x';
      isGameOver = false;
      initializeGame();
    };
    
    const initializeGame = () => {
        if (botFirstToggle.checked) {
            assignRandomO(cells); // Bot makes the first move
        }
    };

    botFirstToggle.addEventListener('change', () => {
        resetBoard();
    });

    cells.forEach(cell => {
      cell.addEventListener('click', handleClick);
    });
    const resetButton = document.getElementById('reset-button');
    resetButton.addEventListener('click', resetBoard);

    initializeGame();
  });