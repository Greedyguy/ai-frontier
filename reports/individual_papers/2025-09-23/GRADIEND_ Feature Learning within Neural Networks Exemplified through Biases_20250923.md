---
keywords:
  - Neural Network
  - Societal Bias
  - Encoder-Decoder Model
  - Model Gradients
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.01406
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:44:40.424760",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Societal Bias",
    "Encoder-Decoder Model",
    "Model Gradients"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.8,
    "Societal Bias": 0.7,
    "Encoder-Decoder Model": 0.75,
    "Model Gradients": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are central to the paper's focus on feature learning and bias correction.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "societal bias",
        "canonical": "Societal Bias",
        "aliases": [
          "social bias",
          "bias in AI"
        ],
        "category": "unique_technical",
        "rationale": "The paper specifically addresses societal biases, making it a unique aspect of the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "encoder-decoder approach",
        "canonical": "Encoder-Decoder Model",
        "aliases": [
          "encoder-decoder architecture"
        ],
        "category": "specific_connectable",
        "rationale": "Encoder-decoder models are a specific architecture used in the paper's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "model gradients",
        "canonical": "Model Gradients",
        "aliases": [
          "gradient-based learning"
        ],
        "category": "unique_technical",
        "rationale": "Model gradients are crucial for the feature learning process described in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "AI systems",
      "critical areas"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "societal bias",
      "resolved_canonical": "Societal Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "encoder-decoder approach",
      "resolved_canonical": "Encoder-Decoder Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "model gradients",
      "resolved_canonical": "Model Gradients",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GRADIEND: Feature Learning within Neural Networks Exemplified through Biases

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01406.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.01406](https://arxiv.org/abs/2502.01406)

## 🔗 유사한 논문
- [[2025-09-23/The Narcissus Hypothesis_Descending to the Rung of Illusion_20250923|The Narcissus Hypothesis:Descending to the Rung of Illusion]] (81.8% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (81.5% similar)
- [[2025-09-22/Where Fact Ends and Fairness Begins_ Redefining AI Bias Evaluation through Cognitive Biases_20250922|Where Fact Ends and Fairness Begins: Redefining AI Bias Evaluation through Cognitive Biases]] (81.5% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (81.0% similar)
- [[2025-09-18/Programmable Cognitive Bias in Social Agents_20250918|Programmable Cognitive Bias in Social Agents]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Encoder-Decoder Model|Encoder-Decoder Model]]
**⚡ Unique Technical**: [[keywords/Societal Bias|Societal Bias]], [[keywords/Model Gradients|Model Gradients]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01406v3 Announce Type: replace-cross 
Abstract: AI systems frequently exhibit and amplify social biases, leading to harmful consequences in critical areas. This study introduces a novel encoder-decoder approach that leverages model gradients to learn a feature neuron encoding societal bias information such as gender, race, and religion. We show that our method can not only identify which weights of a model need to be changed to modify a feature, but even demonstrate that this can be used to rewrite models to debias them while maintaining other capabilities. We demonstrate the effectiveness of our approach across various model architectures and highlight its potential for broader applications.

## 📝 요약

이 연구는 AI 시스템의 사회적 편향 문제를 해결하기 위해 새로운 인코더-디코더 접근 방식을 제안합니다. 이 방법은 모델의 기울기를 활용하여 성별, 인종, 종교와 같은 사회적 편향 정보를 인코딩하는 특징 뉴런을 학습합니다. 연구 결과, 이 방법은 모델의 특정 가중치를 변경하여 편향을 수정할 수 있으며, 다른 기능을 유지하면서 모델을 재작성할 수 있음을 보여줍니다. 다양한 모델 아키텍처에서 이 접근 방식의 효과를 입증하였으며, 더 넓은 응용 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. AI 시스템은 종종 사회적 편견을 증폭시켜 중요한 분야에서 해로운 결과를 초래한다.
- 2. 본 연구는 모델의 기울기를 활용하여 성별, 인종, 종교와 같은 사회적 편향 정보를 인코딩하는 새로운 인코더-디코더 접근법을 소개한다.
- 3. 제안된 방법은 모델의 특정 가중치를 변경하여 특징을 수정할 수 있을 뿐만 아니라, 모델을 재작성하여 편향을 제거하면서도 다른 기능을 유지할 수 있음을 보여준다.
- 4. 다양한 모델 아키텍처에서 제안된 방법의 효과를 입증하고, 더 넓은 응용 가능성을 강조한다.


---

*Generated on 2025-09-24 00:44:40*