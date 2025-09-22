# MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework

**Korean Title:** MedCOD: 사전 체인 강화 프레임워크를 활용한 대형 언어 모델의 영어-스페인어 의료 번역 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Fine-tuning, Structured Prompting

## 🔗 유사한 논문
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (83.3% similar)
- [[2025-09-22/OpenWHO_ A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages_20250922|OpenWHO A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages]] (82.1% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.9% similar)
- [[2025-09-19/A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making_20250919|A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making]] (81.8% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.00934v2 Announce Type: replace-cross 
Abstract: We present MedCOD (Medical Chain-of-Dictionary), a hybrid framework designed to improve English-to-Spanish medical translation by integrating domain-specific structured knowledge into large language models (LLMs). MedCOD integrates domain-specific knowledge from both the Unified Medical Language System (UMLS) and the LLM-as-Knowledge-Base (LLM-KB) paradigm to enhance structured prompting and fine-tuning. We constructed a parallel corpus of 2,999 English-Spanish MedlinePlus articles and a 100-sentence test set annotated with structured medical contexts. Four open-source LLMs (Phi-4, Qwen2.5-14B, Qwen2.5-7B, and LLaMA-3.1-8B) were evaluated using structured prompts that incorporated multilingual variants, medical synonyms, and UMLS-derived definitions, combined with LoRA-based fine-tuning. Experimental results demonstrate that MedCOD significantly improves translation quality across all models. For example, Phi-4 with MedCOD and fine-tuning achieved BLEU 44.23, chrF++ 28.91, and COMET 0.863, surpassing strong baseline models like GPT-4o and GPT-4o-mini. Ablation studies confirm that both MedCOD prompting and model adaptation independently contribute to performance gains, with their combination yielding the highest improvements. These findings highlight the potential of structured knowledge integration to enhance LLMs for medical translation tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.00934v2 발표 유형: 교차 대체  
초록: 우리는 영어-스페인어 의료 번역을 개선하기 위해 도메인별 구조화된 지식을 대형 언어 모델(LLMs)에 통합하는 하이브리드 프레임워크인 MedCOD(의료 사전 체인)를 제시합니다. MedCOD는 구조화된 프롬프트와 미세 조정을 강화하기 위해 통합 의료 언어 시스템(UMLS)과 LLM-지식-기반(LLM-KB) 패러다임 모두에서 도메인별 지식을 통합합니다. 우리는 2,999개의 영어-스페인어 MedlinePlus 기사와 구조화된 의료 맥락으로 주석이 달린 100문장 테스트 세트를 구축했습니다. 네 개의 오픈 소스 LLM(Phi-4, Qwen2.5-14B, Qwen2.5-7B, LLaMA-3.1-8B)은 다국어 변형, 의료 동의어 및 UMLS에서 파생된 정의를 통합한 구조화된 프롬프트를 사용하여 평가되었으며, LoRA 기반의 미세 조정과 결합되었습니다. 실험 결과는 MedCOD가 모든 모델에서 번역 품질을 크게 향상시킨다는 것을 보여줍니다. 예를 들어, MedCOD와 미세 조정을 사용한 Phi-4는 BLEU 44.23, chrF++ 28.91, COMET 0.863을 달성하여 GPT-4o 및 GPT-4o-mini와 같은 강력한 기준 모델을 능가했습니다. 제거 연구는 MedCOD 프롬프트와 모델 적응이 모두 독립적으로 성능 향상에 기여하며, 이들의 결합이 가장 높은 향상을 가져온다는 것을 확인합니다. 이러한 발견은 구조화된 지식 통합이 의료 번역 작업을 위한 LLM을 향상시킬 수 있는 잠재력을 강조합니다.

## 📝 요약

MedCOD는 영어-스페인어 의료 번역을 개선하기 위해 도메인별 구조화된 지식을 대형 언어 모델(LLM)에 통합한 하이브리드 프레임워크입니다. 이 연구는 UMLS와 LLM-KB 패러다임을 활용하여 구조화된 프롬프트와 미세 조정을 통해 번역 품질을 향상시켰습니다. 2,999개의 영어-스페인어 MedlinePlus 기사와 100개의 테스트 문장으로 구성된 병렬 코퍼스를 구축하고, 네 개의 오픈소스 LLM을 평가했습니다. 실험 결과, MedCOD는 모든 모델에서 번역 품질을 크게 향상시켰으며, 특히 Phi-4 모델은 BLEU 44.23, chrF++ 28.91, COMET 0.863을 기록하며 기존 강력한 모델을 능가했습니다. 연구는 MedCOD 프롬프트와 모델 적응이 독립적으로 성능 향상에 기여하며, 두 요소의 결합이 가장 큰 개선을 가져온다는 것을 확인했습니다. 이는 구조화된 지식 통합이 의료 번역 작업에서 LLM의 성능을 향상시킬 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. MedCOD는 UMLS와 LLM-KB 패러다임을 통합하여 영어-스페인어 의료 번역을 개선하는 하이브리드 프레임워크입니다.

- 2. 2,999개의 영어-스페인어 MedlinePlus 기사와 구조화된 의료 문맥이 주석된 100문장 테스트 세트를 구축했습니다.

- 3. MedCOD는 구조화된 프롬프트와 LoRA 기반의 미세 조정을 통해 번역 품질을 크게 향상시켰습니다.

- 4. Phi-4 모델은 MedCOD와 미세 조정을 통해 BLEU 44.23, chrF++ 28.91, COMET 0.863의 성능을 기록하며, 강력한 기준 모델을 능가했습니다.

- 5. 구조화된 지식 통합이 의료 번역 작업에서 LLM의 성능을 향상시킬 잠재력을 가지고 있음을 보여줍니다.

---

*Generated on 2025-09-22 15:00:19*