import json
from kafka import KafkaProducer

# Kafka Producer Configuration
# ใช้ public IP ของ EC2 และ port 29092 ตามที่กำหนดใน Docker Compose
producer = KafkaProducer(
    bootstrap_servers='ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# สร้างข้อมูลที่คุณต้องการส่งไปยัง Kafka Topic3
regions = [
    {"Region_id": 1, "Region_name": "Bangkok", "Population": 5000000, "Area_size": 1500},
    {"Region_id": 2, "Region_name": "Chiang Mai", "Population": 2000000, "Area_size": 2000},
    {"Region_id": 3, "Region_name": "Phuket", "Population": 1000000, "Area_size": 1200},
    {"Region_id": 4, "Region_name": "Khon Kaen", "Population": 1500000, "Area_size": 1800},
    {"Region_id": 5, "Region_name": "Chonburi", "Population": 2500000, "Area_size": 1300},
    {"Region_id": 6, "Region_name": "Songkhla", "Population": 1200000, "Area_size": 1600},
    {"Region_id": 7, "Region_name": "Surat Thani", "Population": 1800000, "Area_size": 2000},
    {"Region_id": 8, "Region_name": "Nakhon Ratchasima", "Population": 3000000, "Area_size": 2500},
    {"Region_id": 9, "Region_name": "Rayong", "Population": 1000000, "Area_size": 1400}
]

# ส่งข้อมูลแต่ละรายการไปยัง Kafka Topic3
def send_to_kafka():
    for region in regions:
        # ส่งข้อมูลที่สร้างไปยัง Kafka Topic3
        producer.send('topic_3', region)
        print(f"Sent to Kafka: {region}")

# เริ่มการส่งข้อมูล
send_to_kafka()
producer.flush()  # ทำการ flush เพื่อให้ข้อมูลส่งเสร็จ