from utils.database import connect_to_database, get_tank_news
from utils.azure_api import get_azure_openai_response
from utils.neo4j_db import Neo4jDatabase
from utils.data_processing import process_news_data, save_to_jsonl

def main():
    # 连接数据库
    connection = connect_to_database()
    if connection is None:
        print("Failed to connect to the database.")
        return

    # 获取新闻数据
    news_data = get_tank_news(connection)
    if not news_data:
        print("No news data found.")
        return

    # 处理新闻数据
    entities = process_news_data(news_data)
    save_to_jsonl(entities, 'data/entities.jsonl')

    # 将实体插入 Neo4j
    neo4j_db = Neo4jDatabase()
    for entity in entities:
        neo4j_db.insert_entity(entity['name'], entity['type'])
    neo4j_db.close()

    # 调用 Azure OpenAI API
    prompt = "请生成一份关于特定主题的简报。"
    response = get_azure_openai_response(prompt)
    if response:
        print("Azure OpenAI Response:", response)

if __name__ == "__main__":
    main()
