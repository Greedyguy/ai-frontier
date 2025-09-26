<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:42:58.521478",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Keyphrase Extraction",
    "Multi-Agent Collaboration",
    "Topic Guidance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Keyphrase Extraction": 0.82,
    "Multi-Agent Collaboration": 0.77,
    "Topic Guidance": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the proposed framework and connect well with existing research on NLP and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Keyphrase Extraction",
        "canonical": "Keyphrase Extraction",
        "aliases": [
          "Keyphrase Identification"
        ],
        "category": "unique_technical",
        "rationale": "Keyphrase extraction is the core task addressed by the MAPEX framework, offering a unique contribution to NLP.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Agent Collaboration",
        "canonical": "Multi-Agent Collaboration",
        "aliases": [
          "Collaborative Agents"
        ],
        "category": "unique_technical",
        "rationale": "The introduction of multi-agent collaboration is a novel approach in keyphrase extraction, enhancing connectivity with AI research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Topic Guidance",
        "canonical": "Topic Guidance",
        "aliases": [
          "Topic-Based Guidance"
        ],
        "category": "specific_connectable",
        "rationale": "Topic guidance is a specific technique used in MAPEX, linking it to topic modeling and NLP strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Keyphrase Extraction",
      "resolved_canonical": "Keyphrase Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Agent Collaboration",
      "resolved_canonical": "Multi-Agent Collaboration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Topic Guidance",
      "resolved_canonical": "Topic Guidance",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MAPEX: A Multi-Agent Pipeline for Keyphrase Extraction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18813.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18813](https://arxiv.org/abs/2509.18813)

## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (85.7% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (85.5% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (85.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.9% similar)
- [[2025-09-23/Robust Native Language Identification through Agentic Decomposition_20250923|Robust Native Language Identification through Agentic Decomposition]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Topic Guidance|Topic Guidance]]
**⚡ Unique Technical**: [[keywords/Keyphrase Extraction|Keyphrase Extraction]], [[keywords/Multi-Agent Collaboration|Multi-Agent Collaboration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18813v1 Announce Type: new 
Abstract: Keyphrase extraction is a fundamental task in natural language processing. However, existing unsupervised prompt-based methods for Large Language Models (LLMs) often rely on single-stage inference pipelines with uniform prompting, regardless of document length or LLM backbone. Such one-size-fits-all designs hinder the full exploitation of LLMs' reasoning and generation capabilities, especially given the complexity of keyphrase extraction across diverse scenarios. To address these challenges, we propose MAPEX, the first framework that introduces multi-agent collaboration into keyphrase extraction. MAPEX coordinates LLM-based agents through modules for expert recruitment, candidate extraction, topic guidance, knowledge augmentation, and post-processing. A dual-path strategy dynamically adapts to document length: knowledge-driven extraction for short texts and topic-guided extraction for long texts. Extensive experiments on six benchmark datasets across three different LLMs demonstrate its strong generalization and universality, outperforming the state-of-the-art unsupervised method by 2.44\% and standard LLM baselines by 4.01\% in F1@5 on average. Code is available at https://github.com/NKU-LITI/MAPEX.

## 📝 요약

이 논문은 자연어 처리에서 중요한 작업인 핵심어 추출을 다루며, 기존의 대규모 언어 모델(LLM) 기반 비지도 학습 방법의 한계를 극복하기 위해 MAPEX라는 새로운 프레임워크를 제안합니다. MAPEX는 다중 에이전트 협업을 통해 문서 길이에 따라 지식 기반 추출과 주제 기반 추출을 동적으로 조정하는 이중 경로 전략을 사용합니다. 실험 결과, MAPEX는 기존 최첨단 비지도 학습 방법보다 평균 2.44%, 표준 LLM 기반보다 4.01% 더 높은 F1@5 성능을 보였습니다. 이 연구는 LLM의 추론 및 생성 능력을 최대한 활용할 수 있는 새로운 방법론을 제시합니다.

## 🎯 주요 포인트

- 1. 기존의 대형 언어 모델(LLM) 기반 비지도 학습 방법은 문서 길이나 LLM 백본에 상관없이 단일 단계 추론 파이프라인에 의존하여 LLM의 잠재력을 충분히 활용하지 못한다.
- 2. MAPEX는 키프레이즈 추출에 다중 에이전트 협업을 도입한 최초의 프레임워크로, 전문가 모집, 후보 추출, 주제 안내, 지식 확장, 후처리 모듈을 통해 LLM 기반 에이전트를 조정한다.
- 3. MAPEX는 문서 길이에 따라 지식 기반 추출(짧은 텍스트)과 주제 기반 추출(긴 텍스트)로 동적으로 적응하는 이중 경로 전략을 사용한다.
- 4. MAPEX는 세 가지 다른 LLM에서 여섯 개의 벤치마크 데이터셋을 통해 기존 최첨단 비지도 학습 방법보다 평균 2.44% F1@5 성능을, 표준 LLM 기준보다 4.01% 향상된 성능을 보여준다.
- 5. MAPEX의 코드는 https://github.com/NKU-LITI/MAPEX에서 제공된다.


---

*Generated on 2025-09-24 15:42:58*