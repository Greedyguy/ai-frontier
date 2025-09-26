<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:29:19.621322",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Attention Mechanism",
    "Semantic Representations",
    "Image Captioning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.9,
    "Attention Mechanism": 0.85,
    "Semantic Representations": 0.78,
    "Image Captioning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models represent a significant evolution in multimodal learning, linking visual and textual data processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Attention Distribution",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Heads"
        ],
        "category": "specific_connectable",
        "rationale": "Attention distribution is crucial for understanding how models prioritize information, directly linking to the core concept of attention mechanisms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Semantic Representations",
        "canonical": "Semantic Representations",
        "aliases": [
          "Semantic Embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Semantic representations are key to understanding how models interpret and encode meaning, offering unique insights into model behavior.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image Captioning",
        "canonical": "Image Captioning",
        "aliases": [
          "Visual Description"
        ],
        "category": "specific_connectable",
        "rationale": "Image captioning is a practical application of vision-language models, linking visual data to linguistic output.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "unidirectional masking mechanism",
      "forward propagation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Attention Distribution",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Semantic Representations",
      "resolved_canonical": "Semantic Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image Captioning",
      "resolved_canonical": "Image Captioning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Mitigating Hallucination in Large Vision-Language Models through Aligning Attention Distribution to Information Flow

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14257.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2505.14257](https://arxiv.org/abs/2505.14257)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization_20250923|Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization]] (88.3% similar)
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (85.1% similar)
- [[2025-09-23/Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models_20250923|Interpreting Attention Heads for Image-to-Text Information Flow in Large Vision-Language Models]] (84.5% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (84.5% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Image Captioning|Image Captioning]]
**⚡ Unique Technical**: [[keywords/Semantic Representations|Semantic Representations]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14257v3 Announce Type: replace 
Abstract: Due to the unidirectional masking mechanism, Decoder-Only models propagate information from left to right. LVLMs (Large Vision-Language Models) follow the same architecture, with visual information gradually integrated into semantic representations during forward propagation. Through systematic analysis, we observe that the majority of the visual information is absorbed into the semantic representations. However, the model's attention distribution does not exhibit sufficient emphasis on semantic representations. This misalignment between the attention distribution and the actual information flow undermines the model's visual understanding ability and contributes to hallucinations. To address this issue, we enhance the model's visual understanding by leveraging the core information embedded in semantic representations. Specifically, we identify attention heads that focus on core semantic representations based on their attention distributions. Then, through a two-stage optimization paradigm, we propagate the advantages of these attention heads across the entire model, aligning the attention distribution with the actual information flow. We evaluate our method on three image captioning benchmarks using five different LVLMs, demonstrating its effectiveness in significantly reducing hallucinations. Further experiments reveal a trade-off between reduced hallucinations and richer details. Notably, our method allows for manual adjustment of the model's conservativeness, enabling flexible control to meet diverse real-world requirements.

## 📝 요약

이 논문은 Decoder-Only 모델의 단방향 마스킹 메커니즘이 시각적 정보의 통합에 미치는 영향을 분석합니다. 연구 결과, 대부분의 시각적 정보는 의미 표현에 흡수되지만, 주의 분포가 의미 표현에 충분히 집중하지 않아 모델의 시각적 이해 능력을 저해하고 환각 현상을 유발함을 발견했습니다. 이를 해결하기 위해, 의미 표현에 내재된 핵심 정보를 활용하여 모델의 시각적 이해를 향상시켰습니다. 주의 분포를 기반으로 핵심 의미 표현에 집중하는 주의 헤드를 식별하고, 두 단계 최적화 패러다임을 통해 모델 전체에 이점을 전파하여 주의 분포와 실제 정보 흐름을 정렬했습니다. 세 가지 이미지 캡셔닝 벤치마크에서 다섯 가지 LVLM을 사용한 평가 결과, 환각 현상을 크게 줄이는 데 효과적임을 입증했습니다. 추가 실험에서는 환각 감소와 세부 정보 풍부함 간의 균형을 확인했으며, 모델의 보수성을 수동 조정하여 다양한 요구사항에 맞출 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. Decoder-Only 모델은 왼쪽에서 오른쪽으로 정보를 전파하며, LVLMs도 같은 구조를 따릅니다.
- 2. 시각 정보가 점진적으로 의미 표현에 통합되지만, 주의 분포가 의미 표현에 충분히 집중되지 않습니다.
- 3. 주의 분포와 실제 정보 흐름의 불일치는 모델의 시각적 이해 능력을 저해하고 환각을 유발합니다.
- 4. 핵심 의미 표현에 집중하는 주의 헤드를 식별하고, 이를 통해 모델 전체의 주의 분포를 실제 정보 흐름과 정렬합니다.
- 5. 제안된 방법은 환각을 줄이면서도 모델의 보수성을 수동으로 조정할 수 있어 다양한 요구에 유연하게 대응할 수 있습니다.


---

*Generated on 2025-09-24 16:29:19*