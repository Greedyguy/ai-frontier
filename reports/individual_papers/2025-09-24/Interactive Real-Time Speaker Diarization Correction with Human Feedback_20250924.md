<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:39:01.571552",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Speaker Diarization Correction",
    "Split-When-Merged Technique",
    "Online Speaker Enrollments"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Speaker Diarization Correction": 0.78,
    "Split-When-Merged Technique": 0.77,
    "Online Speaker Enrollments": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-assisted speaker diarization",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "The use of LLMs for speaker diarization correction connects to broader applications of language models in speech processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "speaker diarization correction",
        "canonical": "Speaker Diarization Correction",
        "aliases": [
          "diarization correction",
          "speaker attribution correction"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application of diarization correction with human feedback, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "split-when-merged technique",
        "canonical": "Split-When-Merged Technique",
        "aliases": [
          "SWM technique",
          "split-merge correction"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach to improving diarization accuracy, making it a specific and unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "online speaker enrollments",
        "canonical": "Online Speaker Enrollments",
        "aliases": [
          "real-time speaker enrollment",
          "dynamic speaker enrollment"
        ],
        "category": "specific_connectable",
        "rationale": "This concept enhances the diarization process by dynamically updating speaker profiles, which is crucial for real-time applications.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "ASR",
      "DER",
      "summary vs full transcript display"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-assisted speaker diarization",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "speaker diarization correction",
      "resolved_canonical": "Speaker Diarization Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "split-when-merged technique",
      "resolved_canonical": "Split-When-Merged Technique",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "online speaker enrollments",
      "resolved_canonical": "Online Speaker Enrollments",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Interactive Real-Time Speaker Diarization Correction with Human Feedback

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18377.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18377](https://arxiv.org/abs/2509.18377)

## 🔗 유사한 논문
- [[2025-09-19/Listening, Imagining \& Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (85.6% similar)
- [[2025-09-18/Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation_20250918|Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation]] (85.0% similar)
- [[2025-09-23/Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing_20250923|Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing]] (81.7% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (80.9% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Online Speaker Enrollments|Online Speaker Enrollments]]
**⚡ Unique Technical**: [[keywords/Speaker Diarization Correction|Speaker Diarization Correction]], [[keywords/Split-When-Merged Technique|Split-When-Merged Technique]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18377v1 Announce Type: new 
Abstract: Most automatic speech processing systems operate in "open loop" mode without user feedback about who said what; yet, human-in-the-loop workflows can potentially enable higher accuracy. We propose an LLM-assisted speaker diarization correction system that lets users fix speaker attribution errors in real time. The pipeline performs streaming ASR and diarization, uses an LLM to deliver concise summaries to the users, and accepts brief verbal feedback that is immediately incorporated without disrupting interactions. Moreover, we develop techniques to make the workflow more effective: First, a split-when-merged (SWM) technique detects and splits multi-speaker segments that the ASR erroneously attributes to just a single speaker. Second, online speaker enrollments are collected based on users' diarization corrections, thus helping to prevent speaker diarization errors from occurring in the future. LLM-driven simulations on the AMI test set indicate that our system substantially reduces DER by 9.92% and speaker confusion error by 44.23%. We further analyze correction efficacy under different settings, including summary vs full transcript display, the number of online enrollments limitation, and correction frequency.

## 📝 요약

이 논문은 실시간 사용자 피드백을 통해 화자 구분 오류를 수정하는 LLM 기반 화자 분할 보정 시스템을 제안합니다. 이 시스템은 스트리밍 음성 인식과 화자 분할을 수행하며, LLM을 사용해 사용자에게 간결한 요약을 제공하고 즉각적인 구두 피드백을 반영합니다. 주요 기법으로는, ASR에서 단일 화자로 잘못 인식된 다중 화자 구간을 분리하는 SWM 기법과 사용자의 수정에 기반한 온라인 화자 등록이 있습니다. AMI 테스트 세트에서 LLM 기반 시뮬레이션 결과, DER이 9.92% 감소하고 화자 혼동 오류가 44.23% 감소했습니다. 다양한 설정에서의 보정 효과도 분석되었습니다.

## 🎯 주요 포인트

- 1. LLM을 활용한 화자 분할 교정 시스템은 사용자가 실시간으로 화자 지정 오류를 수정할 수 있게 합니다.
- 2. SWM 기법을 통해 ASR이 잘못 인식한 다중 화자 구간을 감지하고 분할합니다.
- 3. 사용자의 교정을 기반으로 온라인 화자 등록을 수집하여 미래의 화자 분할 오류를 예방합니다.
- 4. AMI 테스트 세트에서 LLM 기반 시뮬레이션 결과, DER이 9.92% 감소하고 화자 혼동 오류가 44.23% 감소했습니다.
- 5. 요약 대 전체 전사 표시, 온라인 등록 수 제한, 교정 빈도 등 다양한 설정에서 교정 효율성을 분석했습니다.


---

*Generated on 2025-09-24 15:39:01*