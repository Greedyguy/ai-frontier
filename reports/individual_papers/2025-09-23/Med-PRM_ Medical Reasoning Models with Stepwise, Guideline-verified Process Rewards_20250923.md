---
keywords:
  - Large Language Model
  - Retrieval Augmented Generation
  - Clinical Guidelines
  - Medical Reasoning Models
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.11474
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:04:36.583644",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Clinical Guidelines",
    "Medical Reasoning Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.9,
    "Clinical Guidelines": 0.78,
    "Medical Reasoning Models": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to the paper's methodology and are a key concept in natural language processing.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-augmented generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for verifying reasoning steps, linking it to recent advancements in model augmentation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.9
      },
      {
        "surface": "Clinical guidelines",
        "canonical": "Clinical Guidelines",
        "aliases": [
          "Medical Guidelines"
        ],
        "category": "unique_technical",
        "rationale": "Clinical guidelines are used as a verification source, making them a unique aspect of the model's validation process.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Medical reasoning models",
        "canonical": "Medical Reasoning Models",
        "aliases": [
          "Med-PRM"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel framework for medical reasoning, which is central to its contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "process reward modeling",
      "state-of-the-art performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large language models",
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
      "candidate_surface": "Retrieval-augmented generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Clinical guidelines",
      "resolved_canonical": "Clinical Guidelines",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Medical reasoning models",
      "resolved_canonical": "Medical Reasoning Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.11474.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.11474](https://arxiv.org/abs/2506.11474)

## 🔗 유사한 논문
- [[2025-09-23/ReasonMed_ A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning_20250923|ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning]] (87.9% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (87.5% similar)
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (87.2% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (86.8% similar)
- [[2025-09-22/Fleming-R1_ Toward Expert-Level Medical Reasoning via Reinforcement Learning_20250922|Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning]] (86.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Clinical Guidelines|Clinical Guidelines]], [[keywords/Medical Reasoning Models|Medical Reasoning Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11474v2 Announce Type: replace 
Abstract: Large language models have shown promise in clinical decision making, but current approaches struggle to localize and correct errors at specific steps of the reasoning process. This limitation is critical in medicine, where identifying and addressing reasoning errors is essential for accurate diagnosis and effective patient care. We introduce Med-PRM, a process reward modeling framework that leverages retrieval-augmented generation to verify each reasoning step against established medical knowledge bases. By verifying intermediate reasoning steps with evidence retrieved from clinical guidelines and literature, our model can precisely assess the reasoning quality in a fine-grained manner. Evaluations on five medical QA benchmarks and two open-ended diagnostic tasks demonstrate that Med-PRM achieves state-of-the-art performance, with improving the performance of base models by up to 13.50% using Med-PRM. Moreover, we demonstrate the generality of Med-PRM by integrating it in a plug-and-play fashion with strong policy models such as Meerkat, achieving over 80\% accuracy on MedQA for the first time using small-scale models of 8 billion parameters. Our code and data are available at: https://med-prm.github.io/

## 📝 요약

대형 언어 모델은 임상 의사 결정에서 유망하지만, 현재 접근법은 추론 과정의 특정 단계에서 오류를 지역화하고 수정하는 데 어려움을 겪고 있습니다. 이러한 한계는 정확한 진단과 효과적인 환자 치료를 위해 중요한 의학 분야에서 특히 중요합니다. 우리는 Med-PRM이라는 프로세스 보상 모델링 프레임워크를 소개합니다. 이는 검색 보강 생성 방식을 활용하여 각 추론 단계를 확립된 의학 지식 기반과 대조하여 검증합니다. 임상 지침과 문헌에서 검색한 증거로 중간 추론 단계를 검증함으로써, 모델은 세밀한 방식으로 추론의 질을 평가할 수 있습니다. 다섯 개의 의학 QA 벤치마크와 두 개의 개방형 진단 과제 평가에서 Med-PRM은 최대 13.50%의 성능 향상을 이루며 최첨단 성능을 달성했습니다. 또한, Med-PRM은 Meerkat과 같은 강력한 정책 모델에 손쉽게 통합되어, 80% 이상의 정확도로 MedQA에서 소규모 모델(80억 매개변수)로 처음으로 높은 성과를 기록했습니다. 코드와 데이터는 https://med-prm.github.io/에서 이용 가능합니다.

## 🎯 주요 포인트

- 1. Med-PRM은 의료 의사 결정에서 대형 언어 모델의 오류를 식별하고 수정하는 데 도움을 주는 프로세스 보상 모델링 프레임워크입니다.
- 2. 이 프레임워크는 임상 지침과 문헌에서 검색한 증거를 통해 중간 추론 단계를 검증하여 세밀하게 추론 품질을 평가합니다.
- 3. Med-PRM은 5개의 의료 QA 벤치마크와 2개의 개방형 진단 과제에서 기존 모델의 성능을 최대 13.50% 향상시키며 최첨단 성능을 달성했습니다.
- 4. Med-PRM은 Meerkat과 같은 강력한 정책 모델과의 통합을 통해 MedQA에서 80% 이상의 정확도를 처음으로 달성했습니다.
- 5. Med-PRM의 코드는 https://med-prm.github.io/에서 사용할 수 있습니다.


---

*Generated on 2025-09-24 04:04:36*