from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
import app
print(app)  # Should show the location of the app package
