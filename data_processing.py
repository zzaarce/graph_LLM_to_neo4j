import json

def process_news_data(news_data):
    entities = []
    for record in news_data:
        entities.append({
            "name": record.get("name"),
            "type": record.get("type"),
            "related_news": record.get("news_title")
        })
    return entities

def save_to_jsonl(data, filename):
    with open(filename, 'w') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')
