<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:52:40.786588",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Speech",
    "Prosody",
    "Direct Preference Optimization",
    "Group Relative Policy Optimization",
    "Human Preference Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Speech": 0.78,
    "Prosody": 0.77,
    "Direct Preference Optimization": 0.8,
    "Group Relative Policy Optimization": 0.78,
    "Human Preference Optimization": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text-to-speech",
        "canonical": "Text-to-Speech",
        "aliases": [
          "TTS"
        ],
        "category": "broad_technical",
        "rationale": "Text-to-Speech is a foundational technology in the paper, linking it to broader discussions in speech synthesis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "prosody",
        "canonical": "Prosody",
        "aliases": [
          "intonation",
          "speech rhythm"
        ],
        "category": "unique_technical",
        "rationale": "Prosody is a key focus of the paper, crucial for linking discussions on speech naturalness.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Direct Preference Optimization",
        "canonical": "Direct Preference Optimization",
        "aliases": [
          "DPO"
        ],
        "category": "unique_technical",
        "rationale": "Direct Preference Optimization is a novel method introduced in the paper, central to its findings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "Group Relative Policy Optimization is a comparative method discussed, relevant for linking optimization strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "human preference optimization",
        "canonical": "Human Preference Optimization",
        "aliases": [
          "preference-guided learning"
        ],
        "category": "evolved_concepts",
        "rationale": "Human Preference Optimization is an evolved concept in the paper, highlighting the role of human feedback in learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text-to-speech",
      "resolved_canonical": "Text-to-Speech",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "prosody",
      "resolved_canonical": "Prosody",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Direct Preference Optimization",
      "resolved_canonical": "Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "human preference optimization",
      "resolved_canonical": "Human Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# No Verifiable Reward for Prosody: Toward Preference-Guided Prosody Learning in TTS

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18531.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18531](https://arxiv.org/abs/2509.18531)

## 🔗 유사한 논문
- [[2025-09-23/TempFlow-GRPO_ When Timing Matters for GRPO in Flow Models_20250923|TempFlow-GRPO: When Timing Matters for GRPO in Flow Models]] (82.8% similar)
- [[2025-09-23/Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization_20250923|Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization]] (82.7% similar)
- [[2025-09-23/Advancing Speech Understanding in Speech-Aware Language Models with GRPO_20250923|Advancing Speech Understanding in Speech-Aware Language Models with GRPO]] (82.5% similar)
- [[2025-09-23/Preference Distillation via Value based Reinforcement Learning_20250923|Preference Distillation via Value based Reinforcement Learning]] (82.3% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Text-to-Speech|Text-to-Speech]]
**⚡ Unique Technical**: [[keywords/Prosody|Prosody]], [[keywords/Direct Preference Optimization|Direct Preference Optimization]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]]
**🚀 Evolved Concepts**: [[keywords/Human Preference Optimization|Human Preference Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18531v1 Announce Type: cross 
Abstract: Recent work reports gains in neural text-to-speech (TTS) with Group Relative Policy Optimization (GRPO). However, in the absence of a verifiable reward for \textit{prosody}, GRPO trained on transcription-oriented signals (CER/NLL) lowers error rates yet collapses prosody into monotone, unnatural speech; adding speaker-similarity further destabilizes training and degrades CER. We address this with an \textit{iterative Direct Preference Optimization (DPO)} scheme that uses only a few hundred human-labeled preference pairs per round to directly optimize prosodic naturalness while regularizing to the current model. On \textbf{KoCC-TTS}, a curated dataset of authentic Korean call center interactions capturing task-oriented dialogues, our method attains the highest human preference (ELO) with competitive CER, outperforming GRPO and strong commercial baselines. These results suggest that when prosody cannot be rewarded automatically, \textit{human preference optimization} offers a practical and data-efficient path to natural and robust TTS. The demo page is available at \href{https://tts.ch.dev}

## 📝 요약

이 논문은 신경망 기반 텍스트-음성 변환(TTS)에서 Group Relative Policy Optimization(GRPO)의 한계를 극복하기 위해 제안된 방법론을 다룹니다. 기존 GRPO는 전사 지향 신호(CER/NLL)를 사용하여 오류율을 낮추지만, 억양이 단조롭고 부자연스러운 음성을 생성하는 문제점이 있었습니다. 이를 해결하기 위해, 저자들은 인간이 라벨링한 선호 쌍을 활용하여 억양의 자연스러움을 직접 최적화하는 반복적 Direct Preference Optimization(DPO) 방식을 제안했습니다. 이 방법은 한국 콜센터 대화 데이터셋(KoCC-TTS)에서 높은 인간 선호도(ELO)와 경쟁력 있는 CER을 기록하며, GRPO와 상용 기준을 능가하는 성능을 보였습니다. 이는 자동으로 억양을 보상할 수 없는 상황에서 인간 선호 최적화가 자연스럽고 강력한 TTS를 위한 실용적이고 데이터 효율적인 접근법임을 시사합니다.

## 🎯 주요 포인트

- 1. 기존의 GRPO 기반 TTS 모델은 오류율을 낮추지만 단조롭고 부자연스러운 억양을 생성하는 한계를 보입니다.
- 2. 본 연구는 인간이 라벨링한 선호 쌍을 활용한 반복적 Direct Preference Optimization(DPO) 방식을 제안하여 억양의 자연스러움을 직접 최적화합니다.
- 3. KoCC-TTS 데이터셋을 활용한 실험에서 제안된 방법이 GRPO 및 상용 기준 모델보다 높은 인간 선호도(ELO)와 경쟁력 있는 CER을 달성했습니다.
- 4. 자동으로 억양을 보상할 수 없는 상황에서 인간 선호 최적화는 자연스럽고 견고한 TTS를 위한 실용적이고 데이터 효율적인 경로를 제공합니다.


---

*Generated on 2025-09-24 13:52:40*