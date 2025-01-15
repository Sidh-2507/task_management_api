from app import create_app

import sys
print("Python Path:", sys.path)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
