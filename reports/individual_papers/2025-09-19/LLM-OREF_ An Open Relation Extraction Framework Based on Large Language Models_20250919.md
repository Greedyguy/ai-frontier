---
keywords:
  - Large Language Models
  - Open Relation Extraction
  - Relation Discoverer
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15089
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:38:57.628797",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Open Relation Extraction",
    "Relation Discoverer"
  ],
  "rejected_keywords": [
    "Relation Predictor",
    "Self-Correcting Inference Strategy"
  ],
  "similarity_scores": {
    "Large Language Models": 0.88,
    "Open Relation Extraction": 0.82,
    "Relation Discoverer": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models

**Korean Title:** LLM-OREF: 대형 언어 모델 기반의 개방형 관계 추출 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Open Relation Extraction|Open Relation Extraction]], [[keywords/Relation Discoverer|Relation Discoverer]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (80.0% similar)
- [[ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (79.5% similar)
- [[Apertus Democratizing Open and Compliant LLMs for Global Language Environments]] (79.4% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (79.3% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15089v1 Announce Type: new 
Abstract: The goal of open relation extraction (OpenRE) is to develop an RE model that can generalize to new relations not encountered during training. Existing studies primarily formulate OpenRE as a clustering task. They first cluster all test instances based on the similarity between the instances, and then manually assign a new relation to each cluster. However, their reliance on human annotation limits their practicality. In this paper, we propose an OpenRE framework based on large language models (LLMs), which directly predicts new relations for test instances by leveraging their strong language understanding and generation abilities, without human intervention. Specifically, our framework consists of two core components: (1) a relation discoverer (RD), designed to predict new relations for test instances based on \textit{demonstrations} formed by training instances with known relations; and (2) a relation predictor (RP), used to select the most likely relation for a test instance from $n$ candidate relations, guided by \textit{demonstrations} composed of their instances. To enhance the ability of our framework to predict new relations, we design a self-correcting inference strategy composed of three stages: relation discovery, relation denoising, and relation prediction. In the first stage, we use RD to preliminarily predict new relations for all test instances. Next, we apply RP to select some high-reliability test instances for each new relation from the prediction results of RD through a cross-validation method. During the third stage, we employ RP to re-predict the relations of all test instances based on the demonstrations constructed from these reliable test instances. Extensive experiments on three OpenRE datasets demonstrate the effectiveness of our framework. We release our code at https://github.com/XMUDeepLIT/LLM-OREF.git.

## 🔍 Abstract (한글 번역)

arXiv:2509.15089v1 발표 유형: 신규  
초록: 개방형 관계 추출(OpenRE)의 목표는 훈련 중에 접하지 않은 새로운 관계에 일반화할 수 있는 관계 추출(RE) 모델을 개발하는 것입니다. 기존 연구들은 주로 OpenRE를 클러스터링 작업으로 공식화합니다. 이들은 먼저 인스턴스 간의 유사성을 기반으로 모든 테스트 인스턴스를 클러스터링한 후, 각 클러스터에 새로운 관계를 수동으로 할당합니다. 그러나 인간 주석에 의존하는 것은 실용성을 제한합니다. 본 논문에서는 대형 언어 모델(LLM)을 기반으로 한 OpenRE 프레임워크를 제안하며, 이는 인간의 개입 없이 강력한 언어 이해 및 생성 능력을 활용하여 테스트 인스턴스에 대한 새로운 관계를 직접 예측합니다. 구체적으로, 우리의 프레임워크는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) 관계 발견기(RD)는 알려진 관계를 가진 훈련 인스턴스로 구성된 \textit{데모}를 기반으로 테스트 인스턴스에 대한 새로운 관계를 예측하도록 설계되었습니다. (2) 관계 예측기(RP)는 그들의 인스턴스로 구성된 \textit{데모}에 의해 안내되어 $n$개의 후보 관계 중 테스트 인스턴스에 가장 적합한 관계를 선택하는 데 사용됩니다. 새로운 관계를 예측하는 프레임워크의 능력을 향상시키기 위해, 우리는 관계 발견, 관계 노이즈 제거, 관계 예측의 세 단계로 구성된 자기 수정 추론 전략을 설계했습니다. 첫 번째 단계에서는 RD를 사용하여 모든 테스트 인스턴스에 대한 새로운 관계를 예비적으로 예측합니다. 다음으로, 교차 검증 방법을 통해 RD의 예측 결과에서 각 새로운 관계에 대한 높은 신뢰성을 가진 테스트 인스턴스를 선택하기 위해 RP를 적용합니다. 세 번째 단계에서는 이러한 신뢰할 수 있는 테스트 인스턴스로 구성된 데모를 기반으로 모든 테스트 인스턴스의 관계를 다시 예측하기 위해 RP를 사용합니다. 세 가지 OpenRE 데이터셋에 대한 광범위한 실험은 우리의 프레임워크의 효과를 입증합니다. 우리의 코드는 https://github.com/XMUDeepLIT/LLM-OREF.git에서 공개됩니다.

## 📝 요약

이 논문은 새로운 관계 추출(OpenRE) 모델을 제안합니다. 기존 연구는 OpenRE를 클러스터링 작업으로 접근하여, 테스트 인스턴스를 유사성에 따라 클러스터링하고 각 클러스터에 새로운 관계를 수동으로 할당합니다. 그러나 이 방법은 인간의 주석에 의존하여 실용성이 떨어집니다. 이를 해결하기 위해, 본 연구는 대형 언어 모델(LLM)을 활용하여 인간의 개입 없이 테스트 인스턴스의 새로운 관계를 직접 예측하는 OpenRE 프레임워크를 제안합니다. 이 프레임워크는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) 훈련 인스턴스의 관계를 기반으로 테스트 인스턴스의 새로운 관계를 예측하는 '관계 발견기(RD)'와 (2) 후보 관계 중 가장 가능성 높은 관계를 선택하는 '관계 예측기(RP)'입니다. 또한, 관계 발견, 노이즈 제거, 관계 예측의 세 단계로 구성된 자기 수정 추론 전략을 설계하여 새로운 관계 예측 능력을 강화합니다. 세 가지 OpenRE 데이터셋에 대한 실험 결과, 제안된 프레임워크의 효과가 입증되었습니다. 코드도 공개되었습니다.

## 🎯 주요 포인트

- 1. OpenRE의 목표는 훈련 시 접하지 않은 새로운 관계에 일반화할 수 있는 관계 추출 모델을 개발하는 것입니다.

- 2. 기존 연구들은 OpenRE를 주로 클러스터링 작업으로 공식화하며, 테스트 인스턴스를 유사성에 따라 클러스터링하고 각 클러스터에 새로운 관계를 수동으로 할당합니다.

- 3. 본 논문에서는 대형 언어 모델(LLM)을 기반으로 하여 인간의 개입 없이 테스트 인스턴스에 대해 새로운 관계를 직접 예측하는 OpenRE 프레임워크를 제안합니다.

- 4. 제안된 프레임워크는 관계 발견기(RD)와 관계 예측기(RP)라는 두 가지 핵심 구성 요소로 이루어져 있으며, 새로운 관계 예측을 위한 자가 수정 추론 전략을 설계했습니다.

- 5. 세 가지 OpenRE 데이터셋에 대한 광범위한 실험을 통해 제안된 프레임워크의 효과를 입증하였으며, 코드는 공개되어 있습니다.

---

*Generated on 2025-09-19 15:54:27*