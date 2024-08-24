from flask import Flask, jsonify  # For creating the Flask app and returning JSON responses
from pymongo import MongoClient  # For connecting to MongoDB

# Initialize Flask app
app = Flask(__name__)

# Initialize MongoDB client and specify the database and collection
client = MongoClient('mongodb://localhost:27017/')
db = client['Almayadeen']
collection = db['articles']


# 1. Route for getting top keywords
@app.route('/top_keywords', methods=['GET'])
def top_keywords():
    """
    This route handles a GET request to '/top_keywords'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the top 10 most frequent keywords across all documents in the collection.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Unwind the 'keywords' array, creating a document for each keyword
        {"$unwind": "$keywords"},

        # Stage 2: Group by the 'keywords' field and count the occurrences of each keyword
        {
            "$group": {
                "_id": "$keywords",  # Group by the keyword
                "count": {"$sum": 1}  # Count occurrences of each keyword
            }
        },

        # Stage 3: Sort the groups by count in descending order
        {"$sort": {"count": -1}},

        # Stage 4: Limit the result to the top 10 keywords
        {"$limit": 10},

        # Stage 5: Project the results, renaming '_id' to 'keyword' and keeping the 'count'
        {
            "$project": {
                "keyword": "$_id",  # Rename '_id' to 'keyword'
                "count": 1,  # Include the 'count' field
                "_id": 0  # Exclude the original '_id' field
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 2. Route for getting top authors
@app.route('/top_authors', methods=['GET'])
def top_authors():
    """
    This route handles a GET request to '/top_authors'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the top 10 authors who have written the most articles.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Group documents by the 'author' field and count the number of articles for each author
        {
            "$group": {
                "_id": "$author",  # Group by the 'author' field
                "count": {"$sum": 1}  # Count the number of articles for each author
            }
        },
        # Stage 2: Sort the authors by the count of articles in descending order
        {
            "$sort": {"count": -1}
        },
        # Stage 3: Limit the result to the top 10 authors
        {
            "$limit": 10
        },
        # Stage 4: Project the results to show the 'author' and 'count' fields, excluding the default '_id' field
        {
            "$project": {
                "_id": 0,  # Exclude the default '_id' field from the output
                "author": "$_id",  # Rename '_id' to 'author'
                "count": 1  # Include the 'count' field
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 3. Route for getting articles by publication date
@app.route('/articles_by_date', methods=['GET'])
def articles_by_date():
    """
    This route handles a GET request to '/articles_by_date'. It runs an aggregation pipeline on the 'articles' collection
    to group articles by their publication date and return the count of articles for each date.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Convert the 'published_time' to a date string in the format YYYY-MM-DD
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": "%Y-%m-%d",  # Format the date as YYYY-MM-DD
                        "date": {
                            "$dateFromString": {
                                "dateString": "$published_time"  # Convert the 'published_time' string to a date object
                            }
                        }
                    }
                },
                "count": {"$sum": 1}  # Count the number of articles for each date
            }
        },
        # Stage 2: Sort the grouped results by date in ascending order
        {
            "$sort": {
                "_id": 1  # Sort by the date string in ascending order
            }
        },
        # Stage 3: Project the results to include 'date' and 'count', excluding the default '_id' field
        {
            "$project": {
                "_id": 0,  # Exclude the default '_id' field from the output
                "date": "$_id",  # Rename '_id' to 'date'
                "count": 1  # Include the 'count' field
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 4. Route for getting articles by word count
@app.route('/articles_by_word_count', methods=['GET'])
def articles_by_word_count():
    """
    This route handles a GET request to '/articles_by_word_count'. It runs an aggregation pipeline on the 'articles' collection
    to group the articles by word count and return the number of articles for each word count, sorted by word count.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Group by 'word_count' and count the number of articles for each word count
        {
            "$group": {
                "_id": "$word_count",  # Group by word count
                "count": {"$sum": 1}  # Count the number of articles for each word count
            }
        },
        # Stage 2: Sort the results by word count in ascending order
        {
            "$sort": {
                "_id": 1  # Sort by word count (ascending)
            }
        },
        # Stage 3: Project the results to show 'word_count' instead of '_id' and include the 'count'
        {
            "$project": {
                "word_count": "$_id",  # Rename '_id' to 'word_count'
                "count": 1,  # Include the count
                "_id": 0  # Exclude '_id'
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 5. Route for getting articles by language
@app.route('/articles_by_language', methods=['GET'])
def articles_by_language():
    """
    This route handles a GET request to '/articles_by_language'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the number of articles available in each language.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Group by the 'lang' field and count the number of articles for each language
        {
            "$group": {
                "_id": "$lang",  # Group by the language field
                "count": {"$sum": 1}  # Count the number of articles for each language
            }
        },

        # Stage 2: Optionally project the results to rename '_id' to 'language'
        {
            "$project": {
                "language": "$_id",  # Rename '_id' to 'language'
                "count": 1,  # Keep the 'count' field
                "_id": 0  # Exclude the original '_id' field
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 6. Route for getting articles by classes
@app.route('/articles_by_classes', methods=['GET'])
def articles_by_classes():
    """
    This route handles a GET request to '/articles_by_classes'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the number of articles in each class, as specified in the 'classes' field.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Unwind the 'classes' array, creating a document for each class
        {"$unwind": "$classes"},

        # Stage 2: Group by the 'classes.key' field and count the number of articles in each class
        {
            "$group": {
                "_id": "$classes.key",  # Group by the class key
                "count": {"$sum": 1}  # Count the number of articles for each class
            }
        },

        # Stage 3: Project the results, renaming '_id' to 'class' and keeping the 'count'
        {
            "$project": {
                "_id": 0,  # Exclude the original '_id' field
                "class": "$_id",  # Rename '_id' to 'class'
                "count": 1  # Include the 'count' field
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 7. Route for getting recent articles
@app.route('/recent_articles', methods=['GET'])
def recent_articles():
    """
    This route handles a GET request to '/recent_articles'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the 10 most recently published articles.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Sort the articles by 'published_time' in descending order
        {"$sort": {"published_time": -1}},

        # Stage 2: Limit the result to the top 10 most recent articles
        {"$limit": 10},

        # Stage 3: Project the results to include necessary fields (e.g., title, published_time)
        {
            "$project": {
                "_id": 0,  # Exclude the original '_id' field
                "title": 1,  # Include the title of the article
                "published_time": 1  # Include the published time of the article
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 8. Route for getting articles by keyword
@app.route('/articles_by_keyword/<keyword>', methods=['GET'])
def articles_by_keyword(keyword):
    """
    This route handles a GET request to '/articles_by_keyword/<keyword>'. It runs an aggregation pipeline on the 'articles' collection
    to find and return all articles that contain the specified keyword.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Match documents that contain the specified keyword in the 'keywords' array
        {"$match": {"keywords": keyword}},

        # Stage 2: Project the results to include necessary fields (e.g., title)
        {
            "$project": {
                "_id": 0,  # Exclude the original '_id' field
                "title": 1  # Include the title of the article
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 9. Route for getting articles by author
@app.route('/articles_by_author/<author_name>', methods=['GET'])
def articles_by_author(author_name):
    """
    This route handles a GET request to '/articles_by_author/<author_name>'. It runs an aggregation pipeline on the 'articles' collection
    to find and return all articles written by the specified author.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Match documents that are authored by the specified author
        {"$match": {"author": author_name}},

        # Stage 2: Project the results to include necessary fields (e.g., title)
        {
            "$project": {
                "_id": 0,  # Exclude the original '_id' field
                "title": 1  # Include the title of the article
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


# 10. Route for getting articles by class
@app.route('/top_classes', methods=['GET'])
def top_classes():
    """
    This route handles a GET request to '/top_classes'. It runs an aggregation pipeline on the 'articles' collection
    to find and return the top 10 most frequent classes in the articles.
    """
    # Define the aggregation pipeline
    pipeline = [
        # Stage 1: Unwind the 'classes' array, creating a document for each class
        {"$unwind": "$classes"},

        # Stage 2: Group by the 'classes.key' field and count the number of articles for each class
        {
            "$group": {
                "_id": "$classes.key",
                "count": {"$sum": 1}
            }
        },

        # Stage 3: Sort the groups by count in descending order
        {"$sort": {"count": -1}},

        # Stage 4: Limit the result to the top 10 classes
        {"$limit": 10},

        # Stage 5: Project the results, renaming '_id' to 'class' and keeping the 'count'
        {
            "$project": {
                "class": "$_id",
                "count": 1,
                "_id": 0
            }
        }
    ]

    # Execute the aggregation pipeline on the collection
    result = list(collection.aggregate(pipeline))

    # Return the result as a JSON response
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
