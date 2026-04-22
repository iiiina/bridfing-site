import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

content = f"""
<html>
<head>
    <meta charset="UTF-8">
    <title>Daily Briefing</title>
</head>
<body>
    <h1>📊 오늘의 브리핑</h1>
    <p>업데이트 시간: {today}</p>

    <h2>🔥 주요 내용</h2>
    <ul>
        <li>비트코인 시장 변동성 증가</li>
        <li>AI 관련 주 상승세</li>
        <li>글로벌 금리 이슈 지속</li>
    </ul>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("브리핑 생성 완료!")