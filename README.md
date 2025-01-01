# Movie Recommender System

This project is a Movie Recommender System that suggests movies similar to the ones users like. It utilizes machine learning techniques, particularly cosine similarity, to analyze and recommend movies based on their descriptions and metadata.

## Features
- **Movie Recommendation**: Suggests similar movies based on user input.
- **User Interface**: Simple and interactive UI for entering movie names and receiving recommendations.
- **Fast Performance**: Utilizes precomputed similarity matrices for rapid movie suggestions.
- **Scalable**: Can handle a large dataset of movies efficiently.

## Technologies Used
- **Python**
- **Streamlit** - For web interface
- **Pandas** - Data manipulation and analysis
- **Sklearn (Scikit-learn)** - Machine learning library for computing cosine similarity
- **Pickle** - For model and data serialization

## Project Structure
```
├── app.py                         # Main application file
├── movies_dict.pkl                # Serialized movie metadata
├── movies.pkl                     # Serialized movie DataFrame
├── similarity.pkl                 # Precomputed cosine similarity matrix
├── requirements.txt               # List of dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.7+
- Pip (Python package manager)

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Launch the app by running the command above.
2. Enter the name of a movie in the input box.
3. The system will display the top 5 similar movie recommendations.

## Requirements
Here is the list of dependencies required for the project:

```
flask==2.2.5
streamlit==1.30.0
pandas==2.1.4
numpy==1.26.4
scikit-learn==1.2.2
pickle5==0.0.11
```  

*Note*: A more comprehensive list can be found in the `requirements.txt` file.

## How It Works
1. **Data Preparation**: The dataset of movies is processed and stored in `movies.pkl`.
2. **Feature Extraction**: Metadata from movies is vectorized, and cosine similarity is computed.
3. **Recommendation**: When a user inputs a movie name, the system searches for movies with the highest cosine similarity score.

## Model Files
- **movies_dict.pkl**: Contains movie metadata in dictionary format.
- **movies.pkl**: DataFrame storing all movie data.
- **similarity.pkl**: Precomputed similarity matrix for fast recommendations.

## Example
1. Enter the movie "Inception".
2. The system might recommend similar movies like "Interstellar", "The Matrix", etc.

## Future Improvements
- Add support for more metadata like actors, directors, and genres.
- Improve recommendation accuracy using deep learning models.
- Implement collaborative filtering techniques.

## Contributing
Feel free to fork this project and submit pull requests. Contributions are welcome!

## Acknowledgements
- Dataset: Kaggle or IMDB
- Libraries: Scikit-learn, Streamlit, Pandas

