---
keywords:
  - Large Language Model
  - Parameter-Efficient Fine-Tuning
  - Steering Vector Decoding
  - Kullback-Leibler Divergence
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15888
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:18:42.242771",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Parameter-Efficient Fine-Tuning",
    "Steering Vector Decoding",
    "Kullback-Leibler Divergence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Parameter-Efficient Fine-Tuning": 0.8,
    "Steering Vector Decoding": 0.9,
    "Kullback-Leibler Divergence": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Billion-parameter models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader context of language models, facilitating links to related research in NLP and machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "specific_connectable",
        "rationale": "A key technique discussed in the paper, relevant for linking to works on efficient model adaptation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Steering Vector Decoding",
        "canonical": "Steering Vector Decoding",
        "aliases": [
          "SVD"
        ],
        "category": "unique_technical",
        "rationale": "A novel method introduced in the paper, critical for understanding the proposed task adaptation approach.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.9
      },
      {
        "surface": "Kullback-Leibler Divergence",
        "canonical": "Kullback-Leibler Divergence",
        "aliases": [
          "KL Divergence"
        ],
        "category": "specific_connectable",
        "rationale": "A statistical measure used in the method, linking to mathematical foundations in information theory.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "task distribution",
      "output distribution",
      "warm-start"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
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
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Steering Vector Decoding",
      "resolved_canonical": "Steering Vector Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Kullback-Leibler Divergence",
      "resolved_canonical": "Kullback-Leibler Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Distribution-Aligned Decoding for Efficient LLM Task Adaptation

**Korean Title:** 분포 정렬 디코딩을 통한 효율적인 대형 언어 모델 과제 적응

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15888.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15888](https://arxiv.org/abs/2509.15888)

## 🔗 유사한 논문
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (84.3% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (84.0% similar)
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (84.0% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (84.0% similar)
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[keywords/Kullback-Leibler Divergence|Kullback-Leibler Divergence]]
**⚡ Unique Technical**: [[keywords/Steering Vector Decoding|Steering Vector Decoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15888v1 Announce Type: cross 
Abstract: Adapting billion-parameter language models to a downstream task is still costly, even with parameter-efficient fine-tuning (PEFT). We re-cast task adaptation as output-distribution alignment: the objective is to steer the output distribution toward the task distribution directly during decoding rather than indirectly through weight updates. Building on this view, we introduce Steering Vector Decoding (SVD), a lightweight, PEFT-compatible, and theoretically grounded method. We start with a short warm-start fine-tune and extract a task-aware steering vector from the Kullback-Leibler (KL) divergence gradient between the output distribution of the warm-started and pre-trained models. This steering vector is then used to guide the decoding process to steer the model's output distribution towards the task distribution. We theoretically prove that SVD is first-order equivalent to the gradient step of full fine-tuning and derive a globally optimal solution for the strength of the steering vector. Across three tasks and nine benchmarks, SVD paired with four standard PEFT methods improves multiple-choice accuracy by up to 5 points and open-ended truthfulness by 2 points, with similar gains (1-2 points) on commonsense datasets without adding trainable parameters beyond the PEFT adapter. SVD thus offers a lightweight, theoretically grounded path to stronger task adaptation for large language models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15888v1 발표 유형: 교차  
초록: 수십억 개의 매개변수를 가진 언어 모델을 하위 작업에 맞게 조정하는 것은 여전히 비용이 많이 들며, 이는 매개변수 효율적인 미세 조정(PEFT)을 사용하더라도 마찬가지입니다. 우리는 작업 적응을 출력 분포 정렬로 재구성합니다: 목표는 가중치 업데이트를 통해 간접적으로가 아니라 디코딩 중에 직접적으로 출력 분포를 작업 분포로 조정하는 것입니다. 이러한 관점을 바탕으로, 우리는 Steering Vector Decoding (SVD)라는 경량의, PEFT 호환, 이론적으로 근거 있는 방법을 소개합니다. 우리는 짧은 워밍업 미세 조정으로 시작하여 워밍업된 모델과 사전 훈련된 모델의 출력 분포 간의 Kullback-Leibler (KL) 발산 그래디언트로부터 작업 인식 조정 벡터를 추출합니다. 그런 다음 이 조정 벡터를 사용하여 디코딩 과정을 안내하여 모델의 출력 분포를 작업 분포로 조정합니다. 우리는 SVD가 전체 미세 조정의 그래디언트 단계와 1차 동등함을 이론적으로 증명하고, 조정 벡터의 강도에 대한 전역 최적 해를 도출합니다. 세 가지 작업과 아홉 가지 벤치마크에 걸쳐, SVD는 네 가지 표준 PEFT 방법과 결합하여 다지선다형 정확도를 최대 5점, 개방형 진실성을 2점까지 향상시키며, PEFT 어댑터 외에 추가적인 학습 가능한 매개변수를 추가하지 않고 상식 데이터셋에서도 유사한 향상(1-2점)을 보입니다. 따라서 SVD는 대규모 언어 모델에 대한 강력한 작업 적응을 위한 경량의, 이론적으로 근거 있는 경로를 제공합니다.

## 📝 요약

이 논문은 대규모 언어 모델을 다운스트림 작업에 적응시키는 새로운 방법론인 Steering Vector Decoding (SVD)을 제안합니다. SVD는 출력 분포를 작업 분포에 직접 맞추는 방식으로, 파라미터 효율적 미세 조정(PEFT)과 호환됩니다. 이 방법은 Kullback-Leibler 발산의 그래디언트를 이용해 작업 인식 조정 벡터를 추출하고, 이를 통해 모델의 출력 분포를 작업 분포로 유도합니다. SVD는 완전한 미세 조정의 그래디언트 단계와 1차 동등함을 이론적으로 증명하며, 조정 벡터의 최적 강도를 도출합니다. 세 가지 작업과 아홉 가지 벤치마크에서 SVD는 여러 PEFT 방법과 결합하여 선택형 문제 정확도를 최대 5점, 개방형 진실성을 2점 향상시켰습니다. 추가 학습 가능한 파라미터 없이도 상식 데이터셋에서 1-2점의 유사한 향상을 보이며, 대규모 언어 모델의 작업 적응을 강화하는 경량의 이론적 기반을 제공합니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델의 다운스트림 작업 적응을 출력 분포 정렬로 재구성하여 비용을 절감합니다.
- 2. Steering Vector Decoding(SVD) 방법을 도입하여 가벼우면서도 이론적으로 기반이 되는 PEFT 호환 방식을 제공합니다.
- 3. SVD는 워밍업된 모델과 사전 훈련된 모델 간의 KL 발산 기울기에서 작업 인식 조정 벡터를 추출하여 디코딩 과정을 안내합니다.
- 4. SVD는 전체 미세 조정의 기울기 단계와 1차적으로 동등하며, 조정 벡터의 강도에 대한 전역 최적 해를 도출합니다.
- 5. SVD는 PEFT 방법과 결합하여 여러 벤치마크에서 정확도를 최대 5점 향상시키고, 추가 학습 가능한 매개변수 없이도 상식 데이터셋에서 1-2점의 유사한 향상을 제공합니다.


---

*Generated on 2025-09-23 09:18:42*