import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";
import Image from "next/image";

const mbtiOptions = [
  "ENFJ(主人公)", "ENFP(運動家)", "ENTJ(指揮官)", "ENTP(討論者)",
  "INFJ(提唱者)", "INFP(仲介者)", "INTJ(建築家)", "INTP(論理学者)",
  "ESFJ(領事)", "ESFP(エンターテイナー)", "ESTJ(幹部)", "ESTP(起業家)",
  "ISFJ(擁護者)", "ISFP(冒険家)", "ISTJ(ロジスティシャン)", "ISTP(巨匠)"
];

const mbtiData = {
  ENTP: {
    img: "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ENTP.png?raw=true",
    oneLiner: "ぶっ飛び発明家タイプ",
    ai: "アイデア発掘・商品企画AI",
    usage: "おもしろコンテンツづくりや企画出しに",
    feature: "常に刺激を求めて試しまくる",
    position: "新規事業やイノベーション領域、営業企画などに◎"
  },
  // 他タイプも同様に定義していく
};

export default function MBTIApp() {
  const [selected, setSelected] = useState("");
  const code = selected.slice(0, 4);
  const data = mbtiData[code];

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-200 to-cyan-100 p-6">
      <div className="max-w-xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-6">あなたのMBTIは？</h1>
        <Select onValueChange={setSelected}>
          <SelectTrigger className="w-full">
            <SelectValue placeholder="MBTIタイプを選択" />
          </SelectTrigger>
          <SelectContent>
            {mbtiOptions.map((type) => (
              <SelectItem key={type} value={type}>{type}</SelectItem>
            ))}
          </SelectContent>
        </Select>

        {data && (
          <Card className="mt-6 shadow-xl">
            <CardContent className="p-4 space-y-4">
              <Image src={data.img} alt={code} width={400} height={300} className="rounded-xl mx-auto" />
              <h2 className="text-xl font-semibold">{selected} タイプ ✨</h2>
              <p><strong>🌟 一言でいうと:</strong> {data.oneLiner}</p>
              <p><strong>🚀 おすすめAI:</strong> {data.ai}</p>
              <p><strong>🎯 活用スタイル:</strong> {data.usage}</p>
              <p><strong>💡 特徴:</strong> {data.feature}</p>
              <p><strong>🧭 人員配置:</strong> {data.position}</p>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
