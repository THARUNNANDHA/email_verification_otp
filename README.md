# Email Verification with OTP

This project is designed to provide email verification using a one-time password (OTP). It utilizes Flask for web development, Flask-Mail for sending emails, and Flask-SQLAlchemy for managing the database. The OTP is randomly generated and sent to the user's email address for verification.

## Dependencies

- Flask
- Flask-Mail
- Flask-SQLAlchemy

## Features

- Real-time email sending for verification.
- OTP-based email verification process.
- Upon successful verification, users are redirected to the main website.
- Main website showcases a collection of images.
- Images can be downloaded with a single click.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/THARUNNANDHA/email_verification_otp.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Modify `config.py` to specify your database configuration.
   - Run the following commands in the terminal:

   ```bash
   python
   from app import db
   db.create_all()
   exit()
   ```

4. Run the application:

   ```bash
   python app.py
   ```

## Usage

1. Navigate to the application's URL in your web browser.
2. Sign up with your email address.
3. Check your email inbox for the OTP.
4. Enter the received OTP in the verification form.
5. Upon successful verification, you will be redirected to the main website.
6. Explore the collection of images and download them with a single click.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask community
- Flask-Mail developers
- Flask-SQLAlchemy developers
