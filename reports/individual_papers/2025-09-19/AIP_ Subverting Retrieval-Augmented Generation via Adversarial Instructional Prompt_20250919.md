---
keywords:
  - Retrieval-Augmented Generation
  - Large Language Models
  - Adversarial Instructional Prompt
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15159
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:58:36.946265",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval-Augmented Generation",
    "Large Language Models",
    "Adversarial Instructional Prompt"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Retrieval-Augmented Generation": 0.8,
    "Large Language Models": 0.85,
    "Adversarial Instructional Prompt": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt

**Korean Title:** AIP: 적대적 지시 프롬프트를 통한 검색 증강 생성의 전복

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Retrieval-Augmented Generation|Retrieval-Augmented Generation]], [[keywords/Adversarial Instructional Prompt|Adversarial Instructional Prompt]]

## 🔗 유사한 논문
- [[Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (88.4% similar)
- [[GRADA Graph-based Reranking against Adversarial Documents Attack]] (85.7% similar)
- [[Who Taught the Lie Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation]] (84.6% similar)
- [[Engineering RAG Systems for Real-World Applications Design, Development, and Evaluation]] (84.1% similar)
- [[Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (83.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15159v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by retrieving relevant documents from external sources to improve factual accuracy and verifiability. However, this reliance introduces new attack surfaces within the retrieval pipeline, beyond the LLM itself. While prior RAG attacks have exposed such vulnerabilities, they largely rely on manipulating user queries, which is often infeasible in practice due to fixed or protected user inputs. This narrow focus overlooks a more realistic and stealthy vector: instructional prompts, which are widely reused, publicly shared, and rarely audited. Their implicit trust makes them a compelling target for adversaries to manipulate RAG behavior covertly.
  We introduce a novel attack for Adversarial Instructional Prompt (AIP) that exploits adversarial instructional prompts to manipulate RAG outputs by subtly altering retrieval behavior. By shifting the attack surface to the instructional prompts, AIP reveals how trusted yet seemingly benign interface components can be weaponized to degrade system integrity. The attack is crafted to achieve three goals: (1) naturalness, to evade user detection; (2) utility, to encourage use of prompts; and (3) robustness, to remain effective across diverse query variations. We propose a diverse query generation strategy that simulates realistic linguistic variation in user queries, enabling the discovery of prompts that generalize across paraphrases and rephrasings. Building on this, a genetic algorithm-based joint optimization is developed to evolve adversarial prompts by balancing attack success, clean-task utility, and stealthiness. Experimental results show that AIP achieves up to 95.23% ASR while preserving benign functionality. These findings uncover a critical and previously overlooked vulnerability in RAG systems, emphasizing the need to reassess the shared instructional prompts.

## 🔍 Abstract (한글 번역)

arXiv:2509.15159v1 발표 유형: 교차  
초록: Retrieval-Augmented Generation (RAG)은 외부 출처에서 관련 문서를 검색하여 사실적 정확성과 검증 가능성을 향상시킴으로써 대형 언어 모델(LLM)을 강화합니다. 그러나 이러한 의존성은 LLM 자체를 넘어 검색 파이프라인 내에 새로운 공격 표면을 도입합니다. 이전의 RAG 공격은 이러한 취약성을 노출했지만, 주로 사용자 쿼리를 조작하는 데 의존하며, 이는 고정되거나 보호된 사용자 입력으로 인해 실제로는 실행하기 어려운 경우가 많습니다. 이러한 좁은 초점은 보다 현실적이고 은밀한 벡터인 교육적 프롬프트를 간과합니다. 교육적 프롬프트는 널리 재사용되고 공개적으로 공유되며 거의 감사되지 않습니다. 이러한 암묵적인 신뢰는 적대자가 RAG 동작을 은밀하게 조작하기 위한 매력적인 목표가 됩니다.

우리는 적대적 교육 프롬프트(AIP)를 이용하여 검색 동작을 미묘하게 변경함으로써 RAG 출력을 조작하는 새로운 공격을 소개합니다. 공격 표면을 교육적 프롬프트로 전환함으로써 AIP는 신뢰할 수 있지만 겉으로는 무해한 인터페이스 구성 요소가 시스템 무결성을 저하시킬 수 있는 무기로 사용될 수 있음을 드러냅니다. 이 공격은 세 가지 목표를 달성하기 위해 설계되었습니다: (1) 자연스러움, 사용자 탐지를 피하기 위해; (2) 유용성, 프롬프트 사용을 장려하기 위해; (3) 견고성, 다양한 쿼리 변형에 걸쳐 효과를 유지하기 위해. 우리는 사용자 쿼리의 현실적인 언어적 변화를 시뮬레이션하는 다양한 쿼리 생성 전략을 제안하여, 패러프레이즈 및 재구성을 통해 일반화할 수 있는 프롬프트를 발견할 수 있게 합니다. 이를 바탕으로, 공격 성공, 깨끗한 작업의 유용성 및 은밀성을 균형 있게 발전시키기 위해 유전 알고리즘 기반의 공동 최적화를 개발합니다. 실험 결과, AIP는 최대 95.23%의 ASR을 달성하면서도 무해한 기능을 유지하는 것으로 나타났습니다. 이러한 결과는 RAG 시스템에서 중요한 동시에 이전에 간과된 취약성을 밝혀내며, 공유된 교육적 프롬프트를 재평가할 필요성을 강조합니다.

## 📝 요약

이 논문은 Retrieval-Augmented Generation (RAG) 시스템의 새로운 공격 벡터를 제시합니다. 기존의 RAG 공격은 주로 사용자 쿼리 조작에 의존했으나, 이는 실질적으로 어려운 경우가 많습니다. 본 연구는 널리 사용되고 신뢰받는 교육용 프롬프트를 악용하여 RAG의 출력을 조작하는 Adversarial Instructional Prompt (AIP) 공격을 소개합니다. AIP는 자연스러움, 유용성, 견고성을 목표로 하며, 다양한 쿼리 변형에 적응할 수 있는 프롬프트를 생성합니다. 실험 결과, AIP는 최대 95.23%의 공격 성공률을 보이며 시스템의 무결성을 저해할 수 있음을 보여줍니다. 이는 RAG 시스템의 중요한 취약점을 드러내며, 공유된 교육용 프롬프트의 재평가 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation (RAG) 시스템은 외부 문서 검색을 통해 사실 정확성과 검증 가능성을 향상시키지만, 이는 새로운 공격 표면을 도입합니다.

- 2. 기존의 RAG 공격은 주로 사용자 쿼리 조작에 의존했으나, 이는 고정되거나 보호된 사용자 입력 때문에 실질적으로 어려운 경우가 많습니다.

- 3. Adversarial Instructional Prompt (AIP) 공격은 신뢰받는 인터페이스 구성 요소인 지시 프롬프트를 은밀히 조작하여 RAG의 출력을 변형시킵니다.

- 4. AIP는 자연스러움, 유용성, 견고성을 목표로 하여 사용자 탐지를 피하고 다양한 쿼리 변형에 효과적으로 대응합니다.

- 5. 실험 결과, AIP는 최대 95.23%의 공격 성공률을 달성하면서도 정상적인 기능을 유지하여 RAG 시스템의 중요한 취약점을 드러냅니다.

---

*Generated on 2025-09-19 15:56:41*