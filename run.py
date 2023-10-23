from blog import create_app
import os

app = create_app()
port = os.environ.get("PORT", 3000)

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=port)