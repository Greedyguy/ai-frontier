---
keywords:
  - Multimodal Learning
  - Jailbreak Attacks
  - Flowchart Prompts
  - AdaShield Defense
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.21059
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:48:57.528054",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Jailbreak Attacks",
    "Flowchart Prompts",
    "AdaShield Defense"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Jailbreak Attacks": 0.78,
    "Flowchart Prompts": 0.77,
    "AdaShield Defense": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the trending concept of integrating multiple modalities in learning systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "jailbreak attacks",
        "canonical": "Jailbreak Attacks",
        "aliases": [
          "multimodal jailbreak"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel and specific threat vector in the context of MLLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "flowcharts",
        "canonical": "Flowchart Prompts",
        "aliases": [
          "visual prompts",
          "auto-generated flowcharts"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a unique method for inducing specific outputs from MLLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "AdaShield",
        "canonical": "AdaShield Defense",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific defense mechanism against jailbreak attacks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "safety alignment",
      "attack success rate",
      "visual modality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "jailbreak attacks",
      "resolved_canonical": "Jailbreak Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "flowcharts",
      "resolved_canonical": "Flowchart Prompts",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "AdaShield",
      "resolved_canonical": "AdaShield Defense",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# FC-Attack: Jailbreaking Multimodal Large Language Models via Auto-Generated Flowcharts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.21059.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.21059](https://arxiv.org/abs/2502.21059)

## 🔗 유사한 논문
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (87.5% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (85.1% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (85.0% similar)
- [[2025-09-18/MUSE_ MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models_20250918|MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models]] (84.5% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]], [[keywords/Flowchart Prompts|Flowchart Prompts]], [[keywords/AdaShield Defense|AdaShield Defense]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.21059v3 Announce Type: replace-cross 
Abstract: Multimodal Large Language Models (MLLMs) have become powerful and widely adopted in some practical applications. However, recent research has revealed their vulnerability to multimodal jailbreak attacks, whereby the model can be induced to generate harmful content, leading to safety risks. Although most MLLMs have undergone safety alignment, recent research shows that the visual modality is still vulnerable to jailbreak attacks. In our work, we discover that by using flowcharts with partially harmful information, MLLMs can be induced to provide additional harmful details. Based on this, we propose a jailbreak attack method based on auto-generated flowcharts, FC-Attack. Specifically, FC-Attack first fine-tunes a pre-trained LLM to create a step-description generator based on benign datasets. The generator is then used to produce step descriptions corresponding to a harmful query, which are transformed into flowcharts in 3 different shapes (vertical, horizontal, and S-shaped) as visual prompts. These flowcharts are then combined with a benign textual prompt to execute the jailbreak attack on MLLMs. Our evaluations on Advbench show that FC-Attack attains an attack success rate of up to 96% via images and up to 78% via videos across multiple MLLMs. Additionally, we investigate factors affecting the attack performance, including the number of steps and the font styles in the flowcharts. We also find that FC-Attack can improve the jailbreak performance from 4% to 28% in Claude-3.5 by changing the font style. To mitigate the attack, we explore several defenses and find that AdaShield can largely reduce the jailbreak performance but with the cost of utility drop.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLM)의 취약성을 악용하는 멀티모달 탈옥 공격을 다룹니다. 연구진은 부분적으로 유해한 정보를 포함한 플로우차트를 사용하여 MLLM이 추가적인 유해 정보를 생성하도록 유도할 수 있음을 발견했습니다. 이를 바탕으로 자동 생성 플로우차트를 활용한 FC-Attack이라는 공격 방법을 제안했습니다. 이 방법은 사전 학습된 LLM을 미세 조정하여 단계 설명 생성기를 만들고, 이를 통해 유해한 쿼리에 대한 단계 설명을 생성한 후, 이를 시각적 프롬프트로 사용하여 탈옥 공격을 수행합니다. 실험 결과, FC-Attack은 이미지와 비디오를 통해 각각 최대 96%와 78%의 공격 성공률을 기록했습니다. 또한, 플로우차트의 단계 수와 글꼴 스타일이 공격 성능에 영향을 미친다는 것을 밝혔습니다. 방어책으로 AdaShield를 제안했으며, 이는 유틸리티 감소를 초래하지만 탈옥 성능을 크게 줄일 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 다중 모달 대형 언어 모델(MLLMs)은 멀티모달 탈옥 공격에 취약하여 안전성 문제가 발생할 수 있다.
- 2. FC-Attack는 자동 생성된 플로우차트를 활용하여 MLLMs에 대한 탈옥 공격을 수행하는 방법이다.
- 3. FC-Attack는 이미지와 비디오를 통해 각각 최대 96%와 78%의 공격 성공률을 달성한다.
- 4. 플로우차트의 단계 수와 폰트 스타일이 공격 성능에 영향을 미치는 요인으로 밝혀졌다.
- 5. AdaShield는 탈옥 성능을 크게 줄일 수 있지만, 유용성 감소의 비용이 따른다.


---

*Generated on 2025-09-24 00:48:57*