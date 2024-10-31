import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# MySQL 配置
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Azure OpenAI API 配置
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

# Neo4j 配置
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
