<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:15:20.865936",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sa2VA",
    "Sa2VA-i",
    "Referring Video Object Segmentation",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sa2VA": 0.8,
    "Sa2VA-i": 0.85,
    "Referring Video Object Segmentation": 0.78,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sa2VA",
        "canonical": "Sa2VA",
        "aliases": [
          "Sa2VA model"
        ],
        "category": "unique_technical",
        "rationale": "Sa2VA is a unique model central to the paper's contributions and improvements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sa2VA-i",
        "canonical": "Sa2VA-i",
        "aliases": [
          "Improved Sa2VA"
        ],
        "category": "unique_technical",
        "rationale": "Sa2VA-i represents the improved version of the Sa2VA model, a key focus of the paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "referring video object segmentation",
        "canonical": "Referring Video Object Segmentation",
        "aliases": [
          "video object segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific task that the improved model targets, linking it to related works in video segmentation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language models are relevant to the paper's focus on language-guided grounding.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "consistent training",
      "inference procedures",
      "state-of-the-art results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sa2VA",
      "resolved_canonical": "Sa2VA",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sa2VA-i",
      "resolved_canonical": "Sa2VA-i",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "referring video object segmentation",
      "resolved_canonical": "Referring Video Object Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# 3rd Place Report of LSVOS 2025 MeViS Track: Sa2VA-i: Improving Sa2VA Results with Consistent Training and Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19082.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19082](https://arxiv.org/abs/2509.19082)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (91.8% similar)
- [[2025-09-23/The 1st Solution for 7th LSVOS RVOS Track_ SaSaSa2VA_20250923|The 1st Solution for 7th LSVOS RVOS Track: SaSaSa2VA]] (89.4% similar)
- [[2025-09-22/Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge_ 3rd Place Solution_20250922|Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge: 3rd Place Solution]] (84.5% similar)
- [[2025-09-18/SAIL-VL2 Technical Report_20250918|SAIL-VL2 Technical Report]] (84.3% similar)
- [[2025-09-23/SAMSON_ 3rd Place Solution of LSVOS 2025 VOS Challenge_20250923|SAMSON: 3rd Place Solution of LSVOS 2025 VOS Challenge]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Referring Video Object Segmentation|Referring Video Object Segmentation]]
**⚡ Unique Technical**: [[keywords/Sa2VA|Sa2VA]], [[keywords/Sa2VA-i|Sa2VA-i]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19082v1 Announce Type: new 
Abstract: Sa2VA is a recent model for language-guided dense grounding in images and video that achieves state-of-the-art results on multiple segmentation benchmarks and that has become widely popular. However, we found that Sa2VA does not perform according to its full potential for referring video object segmentation tasks. We identify inconsistencies between training and inference procedures as the key factor holding it back. To mitigate this issue, we propose an improved version of Sa2VA, Sa2VA-i, that rectifies these issues and improves the results. In fact, Sa2VA-i sets a new state of the art for multiple video benchmarks and achieves improvements of up to +11.6 J&amp;F on MeViS, +1.4 on Ref-YT-VOS, +3.3 on Ref-DAVIS and +4.1 on ReVOS using the same Sa2VA checkpoints. With our fixes, the Sa2VA-i-1B model even performs on par with the original Sa2VA-26B model on the MeViS benchmark. We hope that this work will show the importance of seemingly trivial implementation details and that it will provide valuable insights for the referring video segmentation field. We provide the code and updated models at https://github.com/kumuji/sa2va-i

## 📝 요약

Sa2VA는 이미지와 비디오에서 언어 기반 밀집 그라운딩을 수행하는 모델로, 여러 세분화 벤치마크에서 최첨단 성능을 보입니다. 그러나 비디오 객체 세분화 작업에서는 잠재력을 충분히 발휘하지 못했습니다. 이는 훈련과 추론 절차 간의 불일치 때문이라고 판단하여, 이를 개선한 Sa2VA-i를 제안했습니다. Sa2VA-i는 여러 비디오 벤치마크에서 새로운 최첨단 성능을 기록했으며, MeViS에서 최대 +11.6 J&F, Ref-YT-VOS에서 +1.4, Ref-DAVIS에서 +3.3, ReVOS에서 +4.1의 성능 향상을 이루었습니다. Sa2VA-i-1B 모델은 MeViS 벤치마크에서 기존 Sa2VA-26B 모델과 동등한 성능을 보입니다. 이 연구는 구현 세부사항의 중요성을 강조하며, 비디오 세분화 분야에 유용한 통찰을 제공할 것입니다. 코드와 업데이트된 모델은 GitHub에서 제공합니다.

## 🎯 주요 포인트

- 1. Sa2VA는 이미지와 비디오에서 언어 기반의 밀집 그라운딩을 위한 최신 모델로 여러 세분화 벤치마크에서 최첨단 결과를 달성했습니다.
- 2. Sa2VA는 비디오 객체 분할 작업에서 최대 성능을 발휘하지 못하며, 이는 훈련과 추론 절차 간의 불일치 때문입니다.
- 3. Sa2VA-i는 이러한 문제를 해결하여 성능을 개선한 Sa2VA의 개선 버전으로, 여러 비디오 벤치마크에서 새로운 최첨단 성능을 설정했습니다.
- 4. Sa2VA-i는 MeViS, Ref-YT-VOS, Ref-DAVIS, ReVOS에서 각각 최대 +11.6, +1.4, +3.3, +4.1의 성능 향상을 달성했습니다.
- 5. 이 연구는 사소해 보이는 구현 세부 사항의 중요성을 보여주고, 비디오 객체 분할 분야에 귀중한 통찰력을 제공하기를 기대합니다.


---

*Generated on 2025-09-24 16:15:20*