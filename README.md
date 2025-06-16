# Reddit Real-Time Analytics with Spark Streaming

A comprehensive real-time analytics solution for analyzing Germany-related discussions on Reddit using Apache Spark Streaming.

## 👥 Team Members
- **Alina Insam**
- **Sumedh Bamane**
- **Rafael Machado Da Rocha**
- **Kaan Ak**

## 📋 Project Overview

This project implements a complete real-time analytics pipeline that:
1. **Streams** Reddit comments from multiple subreddits
2. **Filters** for Germany-related content using 40+ keywords
3. **Processes** data with sentiment analysis and reference extraction
4. **Analyzes** using TF-IDF, peak detection, and controversy analysis
5. **Stores** results in Spark tables and disk files
6. **Visualizes** insights through comprehensive charts and graphs

## 🏗️ Architecture

```
Reddit API → Producer → Socket → Spark Consumer → Analytics & Storage
    ↓           ↓         ↓           ↓               ↓
  PRAW    Filtering   TCP/IP   Structured     Tables + Files
          Sentiment   9998     Streaming      + Visualizations
```

## 📁 Project Structure

```
SparkStreaming Hackathon/
├── Reddit_Assignment_Producer_Alina.ipynb  # Data producer notebook
├── Reddit_Assignment_Consumer.ipynb       # Spark streaming consumer
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
├── data/                                  # Output data directory
│   ├── raw_comments/                      # Raw comment data
│   ├── metrics/                           # Processed metrics
│   └── visualizations/                    # Generated charts
└── logs/                                  # Application logs
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Apache Spark 3.0+
- Java 8/11
- Reddit API credentials

### 1. Environment Setup

```bash
# Clone or download the project
cd "SparkStreaming Hackathon"

# Install Python dependencies
pip install -r requirements.txt

# Download NLTK data for sentiment analysis
python -c "import nltk; nltk.download('vader_lexicon')"
```

### 2. Reddit API Configuration

1. Create a Reddit app at https://www.reddit.com/prefs/apps
2. Update credentials in the producer notebook:
   ```python
   CLIENT_ID = 'your_client_id'
   SECRET_TOKEN = 'your_secret_token'
   USER_AGENT = 'your_user_agent'
   ```

### 3. Running the Pipeline

#### Step 1: Start the Consumer (Spark Streaming)
Open `Reddit_Assignment_Consumer.ipynb` and run all cells to:
- Initialize Spark session with optimized configuration
- Start socket listener on port 9998
- Begin real-time processing pipeline

#### Step 2: Start the Producer (Reddit Stream)
Open `Reddit_Assignment_Producer.ipynb` and run all cells to:
- Connect to Reddit API
- Start streaming Germany-related comments
- Send structured data to consumer via socket

### 4. Monitoring and Analysis

The system will automatically:
- Display real-time statistics and progress
- Save data to Spark tables (`raw` and `metrics`)
- Generate visualizations and reports
- Export CSV files for further analysis

## 🔧 Configuration

### Producer Configuration
```python
CONFIG = {
    'SUBREDDITS': 'europe+worldnews+politics+germany+de+ask_europe',
    'BUFFER_SIZE': 100,
    'WINDOW_SECONDS': 60,
    'MAX_RECONNECT_ATTEMPTS': 5,
    'RECONNECT_DELAY': 5
}
```

### Consumer Configuration
```python
SPARK_CONFIG = {
    'APP_NAME': 'Reddit_Germany_Analytics',
    'BATCH_DURATION': 30,
    'CHECKPOINT_DIR': './checkpoint',
    'OUTPUT_DIR': './data'
}
```

## 📊 Features

### Data Processing
- **Real-time filtering** with 40+ Germany-related keywords
- **Sentiment analysis** using VADER sentiment analyzer
- **Reference extraction** for users, subreddits, and URLs
- **TF-IDF analysis** for top word identification
- **Peak activity detection** and controversy analysis

### Data Storage
- **Spark Tables**: `raw` (all comments) and `metrics` (processed data)
- **File System**: JSON, CSV, and Parquet formats
- **Structured Schema**: Comprehensive data model with metadata

### Visualizations
1. **Sentiment Over Time** - Line chart showing sentiment trends
2. **Word Clouds** - Visual representation of frequent terms
3. **Subreddit Distribution** - Bar chart of comment sources
4. **Sentiment Distribution** - Histogram of sentiment scores
5. **Peak Activity Analysis** - Time-based activity patterns
6. **Reference Analysis** - User mentions and URL sharing patterns
7. **Controversy Detection** - Identification of divisive content
8. **Real-time Metrics Dashboard** - Live statistics display

## 📈 Analytics Capabilities

### Real-time Metrics
- Comment volume and rate tracking
- Sentiment distribution analysis
- Peak activity time detection
- Reference pattern analysis
- Quality score calculation

### Historical Analysis
- Trend identification over time
- Comparative sentiment analysis
- Subreddit activity patterns
- User engagement metrics

### Advanced Features
- **Controversy Detection**: Identifies divisive content using score ratios
- **TF-IDF Word Analysis**: Extracts most significant terms
- **Reference Network Analysis**: Maps user and subreddit mentions
- **Quality Filtering**: Removes low-quality and duplicate content

## 🛠️ Troubleshooting

### Common Issues

1. **Socket Connection Failed**
   ```
   Solution: Ensure consumer is running before starting producer
   Check firewall settings for port 9998
   ```

2. **Reddit API Rate Limiting**
   ```
   Solution: Implement exponential backoff
   Use multiple API credentials if needed
   ```

3. **Spark Memory Issues**
   ```
   Solution: Adjust spark.executor.memory and spark.driver.memory
   Increase checkpoint interval for large datasets
   ```

4. **Missing Dependencies**
   ```bash
   pip install praw textblob vaderSentiment pyspark matplotlib seaborn wordcloud
   ```

### Performance Tuning

- **Batch Size**: Adjust `BATCH_DURATION` based on data volume
- **Memory**: Increase Spark memory allocation for large datasets
- **Parallelism**: Configure `spark.sql.shuffle.partitions`
- **Checkpointing**: Regular checkpoints for fault tolerance

## 📋 Requirements

### Python Packages
```
praw==7.7.1
textblob==0.17.1
vaderSentiment==3.3.2
pyspark==3.4.0
matplotlib==3.7.1
seaborn==0.12.2
wordcloud==1.9.2
pandas==2.0.2
numpy==1.24.3
```

### System Requirements
- **Memory**: Minimum 8GB RAM (16GB recommended)
- **Storage**: 10GB free space for data and logs
- **Network**: Stable internet connection for Reddit API
- **Java**: OpenJDK 8 or 11 for Spark

## 📊 Expected Output

### Data Files
- `raw_comments.json` - All filtered Reddit comments
- `metrics_summary.csv` - Processed analytics data
- `sentiment_trends.json` - Time-series sentiment data
- `word_frequency.csv` - TF-IDF analysis results

### Visualizations
- Real-time dashboard with live metrics
- Sentiment analysis charts and graphs
- Word clouds and frequency distributions
- Activity patterns and peak detection

### Reports
- Comprehensive analytics summary
- Performance statistics and metrics
- Data quality assessment
- Trend analysis and insights

## 🎯 Hackathon Requirements Compliance

✅ **Real-time streaming** via socket connection  
✅ **Raw data storage** in Spark table "raw"  
✅ **TF-IDF analysis** for word extraction and ranking  
✅ **Reference extraction** for users, subreddits, and URLs  
✅ **Sentiment analysis** using VADER sentiment analyzer  
✅ **Metrics storage** in Spark table "metrics"  
✅ **Disk persistence** with multiple output formats  
✅ **Comprehensive visualizations** with 8+ chart types  
✅ **Error handling** and fault tolerance  
✅ **Performance optimization** and monitoring  

## 🔄 Development Workflow

1. **Setup**: Install dependencies and configure credentials
2. **Development**: Modify notebooks for specific requirements
3. **Testing**: Run small-scale tests with limited data
4. **Deployment**: Execute full pipeline with monitoring
5. **Analysis**: Review results and generate reports

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review log files in the `logs/` directory
3. Verify all dependencies are correctly installed
4. Ensure Reddit API credentials are valid

## 🏆 Project Highlights

- **Comprehensive Implementation**: Complete end-to-end pipeline
- **Real-time Processing**: Live data streaming and analysis
- **Advanced Analytics**: TF-IDF, sentiment, and controversy detection
- **Robust Architecture**: Error handling and fault tolerance
- **Rich Visualizations**: Multiple chart types and dashboards
- **Production Ready**: Optimized configuration and monitoring


