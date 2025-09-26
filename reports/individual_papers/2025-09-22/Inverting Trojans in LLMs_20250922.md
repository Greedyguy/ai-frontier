---
keywords:
  - Large Language Model
  - Backdoor Detection
  - Discrete Search
  - Cosine Similarity
  - Trigger Inversion
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16203
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:45:27.301665",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Backdoor Detection",
    "Discrete Search",
    "Cosine Similarity",
    "Trigger Inversion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Backdoor Detection": 0.9,
    "Discrete Search": 0.8,
    "Cosine Similarity": 0.78,
    "Trigger Inversion": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on backdoor detection and inversion.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "backdoor detection",
        "canonical": "Backdoor Detection",
        "aliases": [
          "backdoor inversion"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel method for detecting backdoors in LLMs, which is a unique technical contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "discrete search",
        "canonical": "Discrete Search",
        "aliases": [
          "discrete optimization"
        ],
        "category": "unique_technical",
        "rationale": "Discrete search is a key component of the proposed method for trigger inversion in LLMs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "cosine similarity",
        "canonical": "Cosine Similarity",
        "aliases": [
          "cosine metric"
        ],
        "category": "specific_connectable",
        "rationale": "Cosine similarity is used in the paper to evaluate candidate triggers, linking it to broader applications in vector space analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "trigger inversion",
        "canonical": "Trigger Inversion",
        "aliases": [
          "trigger reversal"
        ],
        "category": "unique_technical",
        "rationale": "Trigger inversion is a unique aspect of the paper's approach to handling backdoors in LLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "gradient-based search",
      "token-length"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "backdoor detection",
      "resolved_canonical": "Backdoor Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "discrete search",
      "resolved_canonical": "Discrete Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cosine similarity",
      "resolved_canonical": "Cosine Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "trigger inversion",
      "resolved_canonical": "Trigger Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Inverting Trojans in LLMs

**Korean Title:** LLM에서 트로이 목마의 반전

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16203.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16203](https://arxiv.org/abs/2509.16203)

## 🔗 유사한 논문
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (84.4% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (83.7% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.6% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.9% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Cosine Similarity|Cosine Similarity]]
**⚡ Unique Technical**: [[keywords/Backdoor Detection|Backdoor Detection]], [[keywords/Discrete Search|Discrete Search]], [[keywords/Trigger Inversion|Trigger Inversion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16203v1 Announce Type: new 
Abstract: While effective backdoor detection and inversion schemes have been developed for AIs used e.g. for images, there are challenges in "porting" these methods to LLMs. First, the LLM input space is discrete, which precludes gradient-based search over this space, central to many backdoor inversion methods. Second, there are ~30,000^k k-tuples to consider, k the token-length of a putative trigger. Third, for LLMs there is the need to blacklist tokens that have strong marginal associations with the putative target response (class) of an attack, as such tokens give false detection signals. However, good blacklists may not exist for some domains. We propose a LLM trigger inversion approach with three key components: i) discrete search, with putative triggers greedily accreted, starting from a select list of singletons; ii) implicit blacklisting, achieved by evaluating the average cosine similarity, in activation space, between a candidate trigger and a small clean set of samples from the putative target class; iii) detection when a candidate trigger elicits high misclassifications, and with unusually high decision confidence. Unlike many recent works, we demonstrate that our approach reliably detects and successfully inverts ground-truth backdoor trigger phrases.

## 🔍 Abstract (한글 번역)

arXiv:2509.16203v1 발표 유형: 신규  
초록: 이미지와 같은 AI에 사용되는 효과적인 백도어 탐지 및 역전 계획이 개발되었지만, 이러한 방법을 대형 언어 모델(LLM)로 "이식"하는 데에는 어려움이 있습니다. 첫째, LLM의 입력 공간은 이산적이어서 많은 백도어 역전 방법의 중심이 되는 이 공간에 대한 그래디언트 기반 탐색을 불가능하게 합니다. 둘째, 고려해야 할 k-튜플은 약 30,000^k개이며, 여기서 k는 가정된 트리거의 토큰 길이입니다. 셋째, LLM의 경우 공격의 가정된 목표 응답(클래스)과 강한 주변 연관성을 가진 토큰을 블랙리스트에 추가해야 하는데, 이러한 토큰은 잘못된 탐지 신호를 제공합니다. 그러나 일부 도메인에서는 적절한 블랙리스트가 존재하지 않을 수 있습니다. 우리는 세 가지 주요 구성 요소를 가진 LLM 트리거 역전 접근법을 제안합니다: i) 단일 항목의 선택 목록에서 시작하여 가정된 트리거를 탐욕적으로 축적하는 이산적 탐색; ii) 가정된 목표 클래스의 작은 깨끗한 샘플 집합과 후보 트리거 사이의 활성화 공간에서 평균 코사인 유사성을 평가하여 달성되는 암묵적 블랙리스트; iii) 후보 트리거가 높은 오분류를 유발하고 비정상적으로 높은 결정 신뢰도를 보일 때의 탐지. 많은 최근 연구와 달리, 우리는 우리의 접근법이 신뢰할 수 있게 탐지하고 실제 백도어 트리거 구문을 성공적으로 역전시킨다는 것을 입증합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 백도어 탐지 및 반전 방법론을 제안합니다. 기존 이미지 기반 AI에서 사용되는 기법을 LLM에 적용하는 데 어려움이 있는데, 이는 LLM의 입력 공간이 이산적이어서 그라디언트 기반 탐색이 불가능하고, 잠재적 트리거의 토큰 길이에 따른 조합이 매우 많으며, 특정 토큰이 공격 대상 클래스와 강한 연관성을 가질 경우 잘못된 탐지 신호를 줄 수 있기 때문입니다. 제안된 방법론은 세 가지 주요 요소로 구성됩니다: i) 단일 토큰 리스트에서 시작해 탐욕적으로 트리거를 구성하는 이산적 탐색, ii) 후보 트리거와 대상 클래스의 샘플 간 코사인 유사도를 평가하여 암묵적으로 블랙리스트 생성, iii) 후보 트리거가 높은 오분류율과 높은 결정 신뢰도를 보일 때 탐지. 이 방법은 기존 연구와 달리 실제 백도어 트리거 문구를 신뢰성 있게 탐지하고 반전할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. LLM의 입력 공간이 이산적이어서 기존의 그래디언트 기반 백도어 탐지 방법을 적용하기 어렵다.
- 2. LLM의 백도어 탐지를 위해서는 강한 주변 연관성을 가진 토큰을 블랙리스트화해야 하지만, 일부 도메인에서는 적절한 블랙리스트가 존재하지 않을 수 있다.
- 3. 제안된 LLM 트리거 역전 방법은 이산적 탐색, 암묵적 블랙리스트, 높은 오분류와 높은 결정 신뢰도를 유발하는 트리거 탐지의 세 가지 주요 구성 요소로 이루어져 있다.
- 4. 제안된 방법은 기존 연구와 달리 실제 백도어 트리거 구문을 신뢰성 있게 탐지하고 성공적으로 역전시킨다.


---

*Generated on 2025-09-23 10:45:27*