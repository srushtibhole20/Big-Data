# Social Media Hashtag Analysis

## Objective
Count the frequency of hashtags in social media posts using Hadoop MapReduce and Python Streaming.

## Files
- `mapper.py` — extracts hashtags.
- `combiner.py` — combines intermediate counts.
- `reducer.py` — calculates final hashtag counts.
- `social_posts.txt` — sample input data.

## Expected Output
```text
#bigdata    3
#hadoop     2
#python     3
#spark      2
```

## Technology
- Apache Hadoop
- HDFS
- Python
- Hadoop Streaming
