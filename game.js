class Game {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.gridSize = 20;
        this.canvas.width = 400;
        this.canvas.height = 400;
        this.snake = [{ x: 10, y: 10 }];
        this.food = { x: 15, y: 15 };
        this.direction = 'right';
        this.score = 0;
        this.gameOver = false;

        document.addEventListener('keydown', this.handleKeyPress.bind(this));
    }

    handleKeyPress(e) {
        switch (e.key) {
            case 'ArrowUp':
                if (this.direction !== 'down') this.direction = 'up';
                break;
            case 'ArrowDown':
                if (this.direction !== 'up') this.direction = 'down';
                break;
            case 'ArrowLeft':
                if (this.direction !== 'right') this.direction = 'left';
                break;
            case 'ArrowRight':
                if (this.direction !== 'left') this.direction = 'right';
                break;
        }
    }

    update() {
        if (this.gameOver) return;

        let head = { ...this.snake[0] };
        switch (this.direction) {
            case 'up':
                head.y--;
                break;
            case 'down':
                head.y++;
                break;
            case 'left':
                head.x--;
                break;
            case 'right':
                head.x++;
                break;
        }

        if (head.x === this.food.x && head.y === this.food.y) {
            this.score++;
            document.getElementById('score').innerText = this.score;
            this.food = {
                x: Math.floor(Math.random() * (this.canvas.width / this.gridSize)),
                y: Math.floor(Math.random() * (this.canvas.height / this.gridSize))
            };
        } else {
            this.snake.pop();
        }

        this.snake.unshift(head);

        for (let i = 1; i < this.snake.length; i++) {
            if (head.x === this.snake[i].x && head.y === this.snake[i].y) {
                this.gameOver = true;
                document.getElementById('gameOver').style.display = 'block';
                return;
            }
        }
    }

    draw() {
        this.ctx.fillStyle = 'black';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.fillStyle = 'green';
        for (let i = 1; i < this.snake.length; i++) {
            this.ctx.fillRect(this.snake[i].x * this.gridSize, this.snake[i].y * this.gridSize, this.gridSize, this.gridSize);
        }

        this.ctx.fillStyle = 'red';
        this.ctx.fillRect(this.snake[0].x * this.gridSize, this.snake[0].y * this.gridSize, this.gridSize, this.gridSize);

        this.ctx.fillStyle = 'blue';
        this.ctx.fillRect(this.food.x * this.gridSize, this.food.y * this.gridSize, this.gridSize, this.gridSize);
    }

    loop() {
        this.update();
        this.draw();
        if (!this.gameOver) {
            setTimeout(this.loop.bind(this), 100);
        }
    }
}
