# DataUp

DataUp is a web application that allows users to upload Excel or CSV files and generates a summary report based on the data in the files. The application is built using Django as the backend framework and utilizes the Pandas library for data manipulation and analysis.

The live demo site is available at [codeman7462.eu.pythonanywhere.com](https://codeman7462.eu.pythonanywhere.com)

## Features

- Upload Excel or CSV files
- Generate a summary report based on the uploaded data
- View summary statistics 
- Uploaded files are stored in media/uploads
## Installation

1. Clone the repository:

```
git clone https://github.com/binaryash/dataup.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Django development server:

```
python manage.py runserver
```

4. Access the application in your web browser at `http://localhost:8000`

## Usage

1. Upload an Excel or CSV file using the provided interface.
2. Click on the "Generate Report" button to generate a summary report.
3. View the summary statistics and insights derived from the uploaded data.
4. Download the summary report in your preferred format.

## Technologies Used

- Django
- Pandas
- HTML
- CSS
- JavaScript

## Approaches Used

- MVT Architecture: Followed the Model-View-Template pattern (similar to MVC) for organizing code and separating concerns.
- Separate Functions for File Handling: Implemented separate functions to read and process the uploaded files. The uploaded files can be in either Excel or CSV format.
- Data Analysis: Leveraged the Pandas library for data manipulation, cleaning, and analysis.
- User Interface Design: Implemented a user-friendly interface using HTML, CSS, and JavaScript.
- File Handling: Managed file uploads and processing using Django's file handling capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.