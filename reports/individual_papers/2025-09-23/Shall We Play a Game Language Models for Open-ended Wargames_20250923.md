---
keywords:
  - Large Language Model
  - Open-ended Wargames
  - Strategic Implications
  - Safety Considerations
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17192
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:57:02.786767",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Open-ended Wargames",
    "Strategic Implications",
    "Safety Considerations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Open-ended Wargames": 0.78,
    "Strategic Implications": 0.77,
    "Safety Considerations": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LMs",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Language Models are central to the paper's exploration of AI in wargames, offering strong connectivity to existing research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Open-ended Wargames",
        "canonical": "Open-ended Wargames",
        "aliases": [
          "Open-ended Games"
        ],
        "category": "unique_technical",
        "rationale": "This term captures a specific type of wargame discussed in the paper, providing a unique angle on game design and AI interaction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Strategic Implications",
        "canonical": "Strategic Implications",
        "aliases": [
          "Strategic Consequences"
        ],
        "category": "unique_technical",
        "rationale": "The strategic implications of decision-making in wargames are a key focus, linking to broader discussions in AI ethics and strategy.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Safety Considerations",
        "canonical": "Safety Considerations",
        "aliases": [
          "Safety Protocols"
        ],
        "category": "specific_connectable",
        "rationale": "Safety considerations are crucial for deploying AI in wargames, aligning with ethical AI deployment practices.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Wargames",
      "Decision-making"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Open-ended Wargames",
      "resolved_canonical": "Open-ended Wargames",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Strategic Implications",
      "resolved_canonical": "Strategic Implications",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Safety Considerations",
      "resolved_canonical": "Safety Considerations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Shall We Play a Game? Language Models for Open-ended Wargames

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17192.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17192](https://arxiv.org/abs/2509.17192)

## 🔗 유사한 논문
- [[2025-09-18/Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem_20250918|Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem]] (81.2% similar)
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (80.0% similar)
- [[2025-09-22/Using Natural Language for Human-Robot Collaboration in the Real World_20250922|Using Natural Language for Human-Robot Collaboration in the Real World]] (80.0% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (79.4% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Safety Considerations|Safety Considerations]]
**⚡ Unique Technical**: [[keywords/Open-ended Wargames|Open-ended Wargames]], [[keywords/Strategic Implications|Strategic Implications]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17192v1 Announce Type: new 
Abstract: Wargames are multi-faceted, multi-player depictions of conflict in which participants' decisions influence future events. Wargames are often used to explore the strategic implications of decision-making. However, it also encompasses entertainment-oriented simulations, ranging from _Chess_ to tabletop role-playing games like _Dungeons & Dragons_ (D&amp;D). On the more open-ended side of the spectrum of wargames, players use natural language to convey their moves, and adjudicators propose outcomes. Language Models (LMs) are increasingly being considered for how they can provide insights into real-world, consequential decisions. We conduct a scoping literature review of a curated selection of 100 recent works on AI in wargames, from which we construct an ontology of wargames in terms of the creativity afforded to either the players or adjudicators. Focusing on the space of wargames with the most open-endedness for players and adjudicators, we distill a set of considerations for when and how to use LMs in different application areas. We also present a set of safety considerations, best practices for deploying LMs in open-ended wargames, and conclude with a set of high-impact open research challenges.

## 📝 요약

이 논문은 전쟁 게임에서 인공지능(AI)의 활용을 탐구하며, 특히 플레이어와 심판에게 창의성을 허용하는 개방형 전쟁 게임에 주목합니다. 100개의 최근 연구를 검토하여 전쟁 게임의 온톨로지를 구축하고, 자연어 처리 모델(LM)을 활용하는 방법과 시기를 제안합니다. 또한, 개방형 전쟁 게임에서 LM을 사용할 때의 안전 고려사항과 모범 사례를 제시하며, 향후 연구 과제를 논의합니다. 주요 기여는 전쟁 게임에서의 AI 활용에 대한 체계적인 분석과 실용적 가이드라인 제공입니다.

## 🎯 주요 포인트

- 1. 워게임은 참가자의 결정이 미래 사건에 영향을 미치는 다면적, 다인용 갈등 묘사로, 전략적 의사결정의 함의를 탐구하는 데 사용된다.
- 2. 워게임은 체스부터 던전 앤 드래곤과 같은 테이블탑 롤플레잉 게임까지 다양한 엔터테인먼트 지향 시뮬레이션을 포함한다.
- 3. 자연어를 사용하여 플레이어의 움직임을 전달하고, 판정자가 결과를 제안하는 개방형 워게임에서 언어 모델(LM)의 활용 가능성을 탐구한다.
- 4. 최근 AI를 활용한 워게임 연구 100편을 검토하여 플레이어와 판정자에게 허용되는 창의성 측면에서 워게임의 온톨로지를 구축하였다.
- 5. 개방형 워게임에서 LM을 사용할 때의 고려사항, 안전성 고려사항, 모범 사례 및 높은 영향력을 가진 연구 과제를 제시한다.


---

*Generated on 2025-09-23 22:57:02*