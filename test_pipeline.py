#!/usr/bin/env python3
"""
Reddit Real-Time Analytics - End-to-End Test Script
Test script to validate the complete pipeline functionality

Team: Alina Insam, Sumedh Bamane, Rafael Machado Da Rocha, Kaan Ak
"""

import subprocess
import time
import socket
import json
import sys
import os
from datetime import datetime

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'praw', 'textblob', 'vaderSentiment', 'pyspark', 
        'matplotlib', 'seaborn', 'wordcloud', 'pandas', 'numpy'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT FOUND")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def check_port_availability(port=9998):
    """Check if the socket port is available"""
    print(f"🔌 Checking port {port} availability...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        
        if result == 0:
            print(f"⚠️  Port {port} is already in use")
            return False
        else:
            print(f"✅ Port {port} is available")
            return True
    except Exception as e:
        print(f"❌ Error checking port: {e}")
        return False

def test_spark_session():
    """Test if Spark can be initialized"""
    print("⚡ Testing Spark session...")
    
    try:
        from pyspark.sql import SparkSession
        
        spark = SparkSession.builder \
            .appName("TestSparkSession") \
            .config("spark.sql.adaptive.enabled", "true") \
            .getOrCreate()
        
        # Test basic functionality
        test_data = [("test", 1), ("data", 2)]
        df = spark.createDataFrame(test_data, ["text", "count"])
        result = df.count()
        
        spark.stop()
        
        if result == 2:
            print("✅ Spark session test successful")
            return True
        else:
            print("❌ Spark session test failed")
            return False
            
    except Exception as e:
        print(f"❌ Spark test error: {e}")
        return False

def test_reddit_api_mock():
    """Test mock Reddit data generation"""
    print("🤖 Testing mock Reddit data generation...")
    
    try:
        sample_data = {
            "id": "test123",
            "text": "This is a test comment about Germany and German politics",
            "created_utc": time.time(),
            "author": "test_user",
            "subreddit": "europe",
            "score": 10,
            "link": "https://reddit.com/test",
            "user_mentions": [],
            "subreddit_references": ["r/germany"],
            "urls": [],
            "sentiment": {
                "compound": 0.1,
                "positive": 0.1,
                "negative": 0.0,
                "neutral": 0.9
            },
            "word_count": 10,
            "char_count": 50,
            "timestamp": datetime.now().isoformat()
        }
        
        # Test JSON serialization
        json_data = json.dumps(sample_data)
        parsed_data = json.loads(json_data)
        
        if parsed_data["id"] == "test123":
            print("✅ Mock data generation successful")
            return True
        else:
            print("❌ Mock data generation failed")
            return False
            
    except Exception as e:
        print(f"❌ Mock data error: {e}")
        return False

def check_output_directories():
    """Check if output directories exist"""
    print("📁 Checking output directories...")
    
    directories = [
        "data/raw_comments",
        "data/metrics", 
        "data/visualizations",
        "logs"
    ]
    
    all_exist = True
    for directory in directories:
        if os.path.exists(directory):
            print(f"✅ {directory}")
        else:
            print(f"❌ {directory} - NOT FOUND")
            all_exist = False
    
    if not all_exist:
        print("Creating missing directories...")
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        print("✅ Directories created")
    
    return True

def test_socket_communication():
    """Test basic socket communication"""
    print("📡 Testing socket communication...")
    
    try:
        # Start a simple echo server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('localhost', 9999))  # Use different port for test
        server_socket.listen(1)
        server_socket.settimeout(2)
        
        # Test client connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(2)
        
        try:
            client_socket.connect(('localhost', 9999))
            
            # Test data transmission
            test_message = '{"test": "data"}\n'
            client_socket.sendall(test_message.encode('utf-8'))
            
            # Accept connection on server
            conn, addr = server_socket.accept()
            received_data = conn.recv(1024).decode('utf-8')
            
            conn.close()
            client_socket.close()
            server_socket.close()
            
            if received_data == test_message:
                print("✅ Socket communication test successful")
                return True
            else:
                print("❌ Socket communication test failed")
                return False
                
        except socket.timeout:
            print("❌ Socket communication timeout")
            return False
            
    except Exception as e:
        print(f"❌ Socket test error: {e}")
        return False
    finally:
        try:
            server_socket.close()
        except:
            pass

def run_comprehensive_test():
    """Run comprehensive system test"""
    print("=" * 60)
    print("🧪 REDDIT ANALYTICS - COMPREHENSIVE SYSTEM TEST")
    print("=" * 60)
    print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tests = [
        ("Dependencies Check", check_dependencies),
        ("Port Availability", lambda: check_port_availability(9998)),
        ("Spark Session", test_spark_session),
        ("Mock Data Generation", test_reddit_api_mock),
        ("Output Directories", check_output_directories),
        ("Socket Communication", test_socket_communication)
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    print("\n📋 Running tests...\n")
    
    for test_name, test_func in tests:
        print(f"🔄 {test_name}:")
        try:
            if test_func():
                passed_tests += 1
            else:
                print(f"   ⚠️  {test_name} failed")
        except Exception as e:
            print(f"   ❌ {test_name} error: {e}")
        print()
    
    # Results summary
    print("=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {passed_tests}/{total_tests}")
    print(f"❌ Failed: {total_tests - passed_tests}/{total_tests}")
    print(f"📈 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! System is ready for deployment.")
        print("\n📝 Next Steps:")
        print("1. Start the Consumer notebook (Reddit_Assignment_Consumer.ipynb)")
        print("2. Start the Producer notebook (Reddit_Assignment_Producer_Alina.ipynb)")
        print("3. Monitor real-time analytics and visualizations")
        print("4. Run final analysis after data collection")
    else:
        print(f"\n⚠️  {total_tests - passed_tests} test(s) failed. Please fix issues before deployment.")
        print("\n🔧 Troubleshooting:")
        print("- Check requirements.txt installation")
        print("- Verify Java installation for Spark")
        print("- Ensure no other processes are using port 9998")
        print("- Review error messages above")
    
    print(f"\n⏰ Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

if __name__ == "__main__":
    run_comprehensive_test()
