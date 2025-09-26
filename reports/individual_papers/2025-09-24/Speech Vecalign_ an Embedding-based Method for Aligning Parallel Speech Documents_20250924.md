<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:38:46.655323",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Speech Vecalign",
    "Speech-to-Speech Translation",
    "Global Mining",
    "Local Mining",
    "VoxPopuli Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Speech Vecalign": 0.8,
    "Speech-to-Speech Translation": 0.9,
    "Global Mining": 0.7,
    "Local Mining": 0.65,
    "VoxPopuli Dataset": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Speech Vecalign",
        "canonical": "Speech Vecalign",
        "aliases": [
          "Vecalign"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, central to its contributions.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "speech-to-speech translation",
        "canonical": "Speech-to-Speech Translation",
        "aliases": [
          "speech translation"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is key to the paper's application and aligns with existing translation models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Global Mining",
        "canonical": "Global Mining",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A baseline method compared against in the study, important for contextual understanding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Local Mining",
        "canonical": "Local Mining",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Another method variant discussed in the paper, relevant for comparative analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      },
      {
        "surface": "VoxPopuli",
        "canonical": "VoxPopuli Dataset",
        "aliases": [
          "VoxPopuli"
        ],
        "category": "unique_technical",
        "rationale": "The dataset used for experiments, crucial for replicability and context.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
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
      "candidate_surface": "Speech Vecalign",
      "resolved_canonical": "Speech Vecalign",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "speech-to-speech translation",
      "resolved_canonical": "Speech-to-Speech Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Global Mining",
      "resolved_canonical": "Global Mining",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Local Mining",
      "resolved_canonical": "Local Mining",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "VoxPopuli",
      "resolved_canonical": "VoxPopuli Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Speech Vecalign: an Embedding-based Method for Aligning Parallel Speech Documents

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18360.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18360](https://arxiv.org/abs/2509.18360)

## 🔗 유사한 논문
- [[2025-09-24/Align Where the Words Look_ Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning_20250924|Align Where the Words Look: Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning]] (80.5% similar)
- [[2025-09-23/Revisiting Speech-Lip Alignment_ A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis_20250923|Revisiting Speech-Lip Alignment: A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis]] (80.4% similar)
- [[2025-09-23/VocSegMRI_ Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI_20250923|VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (79.3% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (79.2% similar)
- [[2025-09-23/Extending Automatic Machine Translation Evaluation to Book-Length Documents_20250923|Extending Automatic Machine Translation Evaluation to Book-Length Documents]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Speech-to-Speech Translation|Speech-to-Speech Translation]]
**⚡ Unique Technical**: [[keywords/Speech Vecalign|Speech Vecalign]], [[keywords/Global Mining|Global Mining]], [[keywords/Local Mining|Local Mining]], [[keywords/VoxPopuli Dataset|VoxPopuli Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18360v1 Announce Type: new 
Abstract: We present Speech Vecalign, a parallel speech document alignment method that monotonically aligns speech segment embeddings and does not depend on text transcriptions. Compared to the baseline method Global Mining, a variant of speech mining, Speech Vecalign produces longer speech-to-speech alignments. It also demonstrates greater robustness than Local Mining, another speech mining variant, as it produces less noise. We applied Speech Vecalign to 3,000 hours of unlabeled parallel English-German (En-De) speech documents from VoxPopuli, yielding about 1,000 hours of high-quality alignments. We then trained En-De speech-to-speech translation models on the aligned data. Speech Vecalign improves the En-to-De and De-to-En performance over Global Mining by 0.37 and 0.18 ASR-BLEU, respectively. Moreover, our models match or outperform SpeechMatrix model performance, despite using 8 times fewer raw speech documents.

## 📝 요약

Speech Vecalign은 텍스트 전사에 의존하지 않고 음성 세그먼트 임베딩을 단조롭게 정렬하는 병렬 음성 문서 정렬 방법입니다. Global Mining과 비교하여 더 긴 음성 간 정렬을 생성하며, Local Mining보다 잡음이 적어 더 견고합니다. VoxPopuli의 3,000시간 분량의 병렬 영어-독일어 음성 문서에 적용하여 약 1,000시간의 고품질 정렬 데이터를 얻었습니다. 이를 바탕으로 영어-독일어 음성 번역 모델을 훈련한 결과, Global Mining 대비 성능이 향상되었으며, 적은 양의 원시 음성 문서를 사용하면서도 SpeechMatrix 모델 성능과 동등하거나 더 우수한 결과를 보였습니다.

## 🎯 주요 포인트

- 1. Speech Vecalign은 텍스트 전사에 의존하지 않고 음성 세그먼트 임베딩을 단조롭게 정렬하는 병렬 음성 문서 정렬 방법입니다.
- 2. Speech Vecalign은 Global Mining과 비교하여 더 긴 음성-음성 정렬을 생성하며, Local Mining보다 더 적은 노이즈로 높은 견고성을 보여줍니다.
- 3. VoxPopuli의 3,000시간의 병렬 영어-독일어 음성 문서에 Speech Vecalign을 적용하여 약 1,000시간의 고품질 정렬 데이터를 얻었습니다.
- 4. 정렬된 데이터를 사용하여 영어-독일어 음성-음성 번역 모델을 훈련한 결과, Global Mining 대비 En-to-De와 De-to-En 성능이 각각 0.37 및 0.18 ASR-BLEU 향상되었습니다.
- 5. Speech Vecalign을 사용한 모델은 8배 적은 원시 음성 문서를 사용하면서도 SpeechMatrix 모델 성능과 동등하거나 더 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 15:38:46*