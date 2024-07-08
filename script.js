document.addEventListener('DOMContentLoaded', (event) => {
    const cells = document.querySelectorAll('.cell');
    let currentPlayer = 'x';
  
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
          currentPlayer = currentPlayer === 'x' ? 'o' : 'x';
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
    };
  
    cells.forEach(cell => {
      cell.addEventListener('click', handleClick);
    });
    const resetButton = document.getElementById('reset-button');
    resetButton.addEventListener('click', resetBoard);
  });