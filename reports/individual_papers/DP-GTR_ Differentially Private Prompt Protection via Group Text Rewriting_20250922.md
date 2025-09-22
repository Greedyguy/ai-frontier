# DP-GTR: Differentially Private Prompt Protection via Group Text Rewriting

**Korean Title:** DP-GTR: 그룹 텍스트 재작성을 통한 차등 프라이버시 프롬프트 보호

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Group Text Rewriting|Group Text Rewriting]] [[keywords/specific/In-context Learning|In-context Learning]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Local Differential Privacy|Local Differential Privacy]] [[keywords/unique/DP-GTR|DP-GTR]] [[categories/cs.CL|cs.CL]] [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench: A Benchmark for Differentially Private Text Generation]] (85.0% similar) [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.7% similar) [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA: Graph-based Reranking against Adversarial Documents Attack]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Group Text Rewriting
**🔗 Specific Connectable**: In-context Learning
**🔬 Broad Technical**: Large Language Models, Local Differential Privacy
**⭐ Unique Technical**: DP-GTR
## 🔗 유사한 논문
- [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench A Benchmark for Differentially Private Text Generation]] (85.0% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.7% similar)
- [[2025-09-19/GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA Graph-based Reranking against Adversarial Documents Attack]] (82.5% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (81.5% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (81.3% similar)


**ArXiv ID**: [2503.04990](https://arxiv.org/abs/2503.04990)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2503.04990.pdf)


**ArXiv ID**: [2503.04990](https://arxiv.org/abs/2503.04990)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2503.04990.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Group Text Rewriting
**🔗 Specific Connectable**: In-context Learning
**⭐ Unique Technical**: DP-GTR
**🔬 Broad Technical**: Large Language Models, Local Differential Privacy

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Local Differential Privacy` • 

`In-context Learning` • 

`DP-GTR` • 

`Group Text Rewriting`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04990v2 Announce Type: replace 
Abstract: Prompt privacy is crucial, especially when using online large language models (LLMs), due to the sensitive information often contained within prompts. While LLMs can enhance prompt privacy through text rewriting, existing methods primarily focus on document-level rewriting, neglecting the rich, multi-granular representations of text. This limitation restricts LLM utilization to specific tasks, overlooking their generalization and in-context learning capabilities, thus hindering practical application. To address this gap, we introduce DP-GTR, a novel three-stage framework that leverages local differential privacy (DP) and the composition theorem via group text rewriting. DP-GTR is the first framework to integrate both document-level and word-level information while exploiting in-context learning to simultaneously improve privacy and utility, effectively bridging local and global DP mechanisms at the individual data point level. Experiments on CommonSense QA and DocVQA demonstrate that DP-GTR outperforms existing approaches, achieving a superior privacy-utility trade-off. Furthermore, our framework is compatible with existing rewriting techniques, serving as a plug-in to enhance privacy protection. Our code is publicly available at github.com/ResponsibleAILab/DP-GTR.

## 🔍 Abstract (한글 번역)

arXiv:2503.04990v2 발표 유형: 교체  
초록: 프롬프트 프라이버시는 특히 온라인 대형 언어 모델(LLMs)을 사용할 때 프롬프트에 종종 포함된 민감한 정보 때문에 매우 중요합니다. LLM은 텍스트 재작성을 통해 프롬프트 프라이버시를 강화할 수 있지만, 기존 방법은 주로 문서 수준의 재작성에 초점을 맞추고 있어 텍스트의 풍부하고 다중 세분화된 표현을 간과하고 있습니다. 이러한 제한은 LLM의 활용을 특정 작업으로 제한하여 일반화 및 맥락 내 학습 능력을 간과하게 하여 실질적인 응용을 저해합니다. 이러한 격차를 해결하기 위해, 우리는 그룹 텍스트 재작성을 통해 지역 차등 프라이버시(DP)와 구성 정리를 활용하는 새로운 3단계 프레임워크인 DP-GTR을 소개합니다. DP-GTR은 문서 수준과 단어 수준의 정보를 모두 통합하고 맥락 내 학습을 활용하여 프라이버시와 유틸리티를 동시에 개선하는 첫 번째 프레임워크로, 개별 데이터 포인트 수준에서 지역 및 글로벌 DP 메커니즘을 효과적으로 연결합니다. CommonSense QA와 DocVQA에 대한 실험 결과, DP-GTR은 기존 접근 방식을 능가하여 우수한 프라이버시-유틸리티 균형을 달성합니다. 또한, 우리의 프레임워크는 기존의 재작성 기술과 호환되어 프라이버시 보호를 강화하는 플러그인으로 작동합니다. 우리의 코드는 github.com/ResponsibleAILab/DP-GTR에서 공개적으로 이용 가능합니다.

## 📝 요약

이 논문은 온라인 대형 언어 모델(LLM) 사용 시 프롬프트에 포함된 민감한 정보의 보호를 위한 프롬프트 프라이버시의 중요성을 강조합니다. 기존 방법은 주로 문서 수준의 재작성에 집중하여 LLM의 일반화 및 맥락 내 학습 능력을 충분히 활용하지 못했습니다. 이를 해결하기 위해, 저자들은 DP-GTR이라는 새로운 3단계 프레임워크를 제안했습니다. 이 프레임워크는 로컬 차등 프라이버시(DP)와 그룹 텍스트 재작성을 통한 조합 정리를 활용하여 문서 수준과 단어 수준의 정보를 통합합니다. CommonSense QA와 DocVQA 실험에서 DP-GTR은 기존 방법보다 우수한 프라이버시-유틸리티 균형을 달성했으며, 기존의 재작성 기술과 호환되어 프라이버시 보호를 강화할 수 있습니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트


- 1. 온라인 대형 언어 모델(LLM) 사용 시 프롬프트에 포함된 민감한 정보를 보호하기 위해 프롬프트 프라이버시가 중요하다.

- 2. 기존 방법은 문서 수준의 재작성을 중심으로 하여 LLM의 일반화 및 맥락 내 학습 능력을 충분히 활용하지 못한다.

- 3. DP-GTR은 로컬 차등 프라이버시(DP)와 그룹 텍스트 재작성을 통해 프라이버시와 유틸리티를 동시에 개선하는 새로운 프레임워크이다.

- 4. DP-GTR은 문서 수준과 단어 수준의 정보를 통합하여 기존 방법보다 우수한 프라이버시-유틸리티 균형을 달성한다.

- 5. DP-GTR은 기존의 재작성 기술과 호환 가능하며, 프라이버시 보호를 강화하는 플러그인으로 활용될 수 있다.


---

*Generated on 2025-09-22 16:35:14*