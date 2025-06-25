<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MBTI AIレコメンド</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(to bottom, #b3d9ea, #e0f7fa);
      color: #4A4A4A;
      padding: 2rem;
    }
    .container {
      max-width: 700px;
      margin: auto;
    }
    .card {
      background: rgba(255, 255, 255, 0.95);
      padding: 2rem;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      margin-top: 2rem;
    }
    select, button {
      width: 100%;
      padding: 1rem;
      margin-top: 1rem;
      border: none;
      border-radius: 10px;
      font-size: 1rem;
    }
    button {
      background-color: #4A90E2;
      color: white;
      cursor: pointer;
    }
    button:hover {
      background-color: #357ABD;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>あなたのMBTIタイプを選んでください</h1>
    <select id="mbti-select">
      <option value="">-- MBTIタイプを選択 --</option>
      <option value="ENFP">ENFP (運動家)</option>
      <option value="INTJ">INTJ (建築家)</option>
      <option value="ENTP">ENTP (討論者)</option>
      <option value="ISFJ">ISFJ (擁護者)</option>
      <!-- 他のMBTIも必要に応じて追加 -->
    </select>
    <button onclick="showAdvice()">診断スタート</button>

    <div id="result" class="card" style="display: none;"></div>
  </div>

  <script>
    const advice = {
      ENFP: {
        title: "ENFP - 感性のバクハツ系アイデアマン",
        ai: "ビジュアル系AI、創造系チャットボット",
        style: "発想のブレストやSNS投稿にも",
        job: "マーケ・PR・イベント・スタートアップ系など自由度の高い環境◎"
      },
      INTJ: {
        title: "INTJ - 思考のアーキテクト",
        ai: "戦略設計AI、論文生成や構造化系AI",
        style: "計画立案、研究支援、裏方で大活躍",
        job: "戦略立案や企画設計、研究職や経営企画も◎"
      },
      ENTP: {
        title: "ENTP - ぶっ飛び発明家タイプ",
        ai: "アイデア発掘・商品企画AI",
        style: "コンテンツづくりや企画出しに",
        job: "新規事業やイノベーション、営業企画など"
      },
      ISFJ: {
        title: "ISFJ - サポートのプロフェッショナル",
        ai: "翻訳・要約AI、事務補助系ツール",
        style: "地道に正確な作業を助ける方向で",
        job: "医療・事務・秘書など、人に寄り添う配置"
      }
    };

    function showAdvice() {
      const mbti = document.getElementById('mbti-select').value;
      const resultDiv = document.getElementById('result');

      if (mbti && advice[mbti]) {
        const data = advice[mbti];
        resultDiv.innerHTML = `
          <h2>${data.title}</h2>
          <p><strong>🌟 おすすめAI:</strong> ${data.ai}</p>
          <p><strong>🎯 活用スタイル:</strong> ${data.style}</p>
          <p><strong>🧭 向いている人員配置:</strong> ${data.job}</p>
        `;
        resultDiv.style.display = 'block';
      } else {
        resultDiv.innerHTML = '<p>タイプを選んでください！</p>';
        resultDiv.style.display = 'block';
      }
    }
  </script>
</body>
</html>
