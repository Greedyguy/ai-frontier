<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:35:32.289969",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LaMP-Cap",
    "Multimodal Learning",
    "Personalized Caption Generation",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LaMP-Cap": 0.8,
    "Multimodal Learning": 0.85,
    "Personalized Caption Generation": 0.78,
    "Large Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LaMP-Cap",
        "canonical": "LaMP-Cap",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "LaMP-Cap is a unique dataset introduced in the paper, crucial for personalized figure caption generation with multimodal profiles.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Figure Profiles",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Profiles"
        ],
        "category": "specific_connectable",
        "rationale": "The use of multimodal figure profiles is central to the paper's approach, linking it to the broader concept of multimodal learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Personalized Figure Caption Generation",
        "canonical": "Personalized Caption Generation",
        "aliases": [
          "Figure Caption Personalization"
        ],
        "category": "unique_technical",
        "rationale": "This concept is a unique application of personalization in AI, specifically targeting figure captions.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a foundational technology used in the experiments, providing a basis for understanding the paper's methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "figure",
      "caption",
      "dataset",
      "profile"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LaMP-Cap",
      "resolved_canonical": "LaMP-Cap",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Figure Profiles",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Personalized Figure Caption Generation",
      "resolved_canonical": "Personalized Caption Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# LaMP-Cap: Personalized Figure Caption Generation With Multimodal Figure Profiles

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.06561.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2506.06561](https://arxiv.org/abs/2506.06561)

## 🔗 유사한 논문
- [[2025-09-24/Improving Image Captioning Descriptiveness by Ranking and LLM-based Fusion_20250924|Improving Image Captioning Descriptiveness by Ranking and LLM-based Fusion]] (82.7% similar)
- [[2025-09-23/LaMP-QA_ A Benchmark for Personalized Long-form Question Answering_20250923|LaMP-QA: A Benchmark for Personalized Long-form Question Answering]] (82.5% similar)
- [[2025-09-22/RePIC_ Reinforced Post-Training for Personalizing Multi-Modal Language Models_20250922|RePIC: Reinforced Post-Training for Personalizing Multi-Modal Language Models]] (82.2% similar)
- [[2025-09-23/ComposeMe_ Attribute-Specific Image Prompts for Controllable Human Image Generation_20250923|ComposeMe: Attribute-Specific Image Prompts for Controllable Human Image Generation]] (81.8% similar)
- [[2025-09-23/Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model_20250923|Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/LaMP-Cap|LaMP-Cap]], [[keywords/Personalized Caption Generation|Personalized Caption Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.06561v4 Announce Type: replace-cross 
Abstract: Figure captions are crucial for helping readers understand and remember a figure's key message. Many models have been developed to generate these captions, helping authors compose better quality captions more easily. Yet, authors almost always need to revise generic AI-generated captions to match their writing style and the domain's style, highlighting the need for personalization. Despite language models' personalization (LaMP) advances, these technologies often focus on text-only settings and rarely address scenarios where both inputs and profiles are multimodal. This paper introduces LaMP-Cap, a dataset for personalized figure caption generation with multimodal figure profiles. For each target figure, LaMP-Cap provides not only the needed inputs, such as figure images, but also up to three other figures from the same document--each with its image, caption, and figure-mentioning paragraphs--as a profile to characterize the context. Experiments with four LLMs show that using profile information consistently helps generate captions closer to the original author-written ones. Ablation studies reveal that images in the profile are more helpful than figure-mentioning paragraphs, highlighting the advantage of using multimodal profiles over text-only ones.

## 📝 요약

이 논문은 개인화된 그림 캡션 생성을 위한 데이터셋인 LaMP-Cap을 소개합니다. LaMP-Cap은 그림 이미지뿐만 아니라 동일 문서 내 다른 그림들의 이미지, 캡션, 관련 문단을 프로파일로 제공하여 문맥을 파악할 수 있게 합니다. 실험 결과, 프로파일 정보를 활용하면 원 저자가 작성한 캡션에 더 가까운 결과를 생성할 수 있으며, 이미지가 텍스트보다 더 유용하다는 것을 발견했습니다. 이는 멀티모달 프로파일의 장점을 강조합니다.

## 🎯 주요 포인트

- 1. 그림 캡션은 독자가 그림의 핵심 메시지를 이해하고 기억하는 데 중요한 역할을 한다.
- 2. AI로 생성된 캡션은 작성자의 스타일과 도메인 스타일에 맞게 수정이 필요하여 개인화의 필요성이 강조된다.
- 3. LaMP-Cap은 멀티모달 그림 프로필을 활용한 개인화된 그림 캡션 생성을 위한 데이터셋을 소개한다.
- 4. 실험 결과, 프로필 정보를 활용하면 원저자 작성 캡션에 더 가까운 캡션을 생성할 수 있다.
- 5. 프로필 내 이미지가 텍스트만 있는 경우보다 캡션 생성에 더 유용하다는 점이 드러났다.


---

*Generated on 2025-09-24 14:35:32*