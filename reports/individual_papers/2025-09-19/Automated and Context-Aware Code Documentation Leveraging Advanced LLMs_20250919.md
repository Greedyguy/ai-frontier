
# Automated and Context-Aware Code Documentation Leveraging Advanced LLMs

**Korean Title:** 고급 LLM을 활용한 자동화 및 상황 인식 코드 문서화

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Template-based Documentation, Context-aware Javadoc Generation

## 🔗 유사한 논문
- [[MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (83.7% similar)
- [[LLM Agents for Interactive Workflow Provenance Reference Architecture and Evaluation Methodology]] (82.5% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.3% similar)
- [[Automating Modelica Module Generation Using Large Language Models A Case Study on Building Control Description Language]] (81.9% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (81.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14273v1 Announce Type: new 
Abstract: Code documentation is essential to improve software maintainability and comprehension. The tedious nature of manual code documentation has led to much research on automated documentation generation. Existing automated approaches primarily focused on code summarization, leaving a gap in template-based documentation generation (e.g., Javadoc), particularly with publicly available Large Language Models (LLMs). Furthermore, progress in this area has been hindered by the lack of a Javadoc-specific dataset that incorporates modern language features, provides broad framework/library coverage, and includes necessary contextual information. This study aims to address these gaps by developing a tailored dataset and assessing the capabilities of publicly available LLMs for context-aware, template-based Javadoc generation. In this work, we present a novel, context-aware dataset for Javadoc generation that includes critical structural and semantic information from modern Java codebases. We evaluate five open-source LLMs (including LLaMA-3.1, Gemma-2, Phi-3, Mistral, Qwen-2.5) using zero-shot, few-shot, and fine-tuned setups and provide a comparative analysis of their performance. Our results demonstrate that LLaMA 3.1 performs consistently well and is a reliable candidate for practical, automated Javadoc generation, offering a viable alternative to proprietary systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.14273v1 발표 유형: 신규  
초록: 코드 문서는 소프트웨어의 유지보수성과 이해도를 향상시키기 위해 필수적입니다. 수작업으로 코드 문서를 작성하는 것은 지루한 작업이기 때문에 자동화된 문서 생성에 대한 많은 연구가 이루어졌습니다. 기존의 자동화된 접근 방식은 주로 코드 요약에 초점을 맞추고 있어, 특히 공개적으로 사용 가능한 대형 언어 모델(LLMs)을 활용한 템플릿 기반 문서 생성(예: Javadoc)에는 공백이 존재합니다. 더욱이, 이 분야의 발전은 현대 언어 기능을 통합하고, 광범위한 프레임워크/라이브러리 커버리지를 제공하며, 필요한 맥락 정보를 포함하는 Javadoc 전용 데이터세트의 부족으로 인해 저해되었습니다. 본 연구는 맞춤형 데이터세트를 개발하고, 공개적으로 사용 가능한 LLM의 맥락 인식 템플릿 기반 Javadoc 생성 능력을 평가함으로써 이 공백을 해결하는 것을 목표로 합니다. 본 연구에서는 현대 Java 코드베이스의 중요한 구조적 및 의미적 정보를 포함하는 참신하고 맥락 인식이 가능한 Javadoc 생성 데이터세트를 제시합니다. 우리는 LLaMA-3.1, Gemma-2, Phi-3, Mistral, Qwen-2.5를 포함한 다섯 개의 오픈소스 LLM을 제로샷, 몇샷, 그리고 미세 조정된 설정에서 평가하고, 그 성능에 대한 비교 분석을 제공합니다. 우리의 결과는 LLaMA 3.1이 일관되게 우수한 성능을 발휘하며, 실용적이고 자동화된 Javadoc 생성에 있어 신뢰할 수 있는 후보임을 보여주며, 독점 시스템에 대한 실질적인 대안을 제공합니다.

## 📝 요약

이 연구는 코드 문서화 자동화를 위한 Javadoc 생성에 초점을 맞추고 있습니다. 기존의 자동화 접근법은 주로 코드 요약에 집중되어 있어, Javadoc과 같은 템플릿 기반 문서 생성에는 한계가 있었습니다. 이를 해결하기 위해 현대 자바 코드베이스의 구조적 및 의미적 정보를 포함한 새로운 데이터셋을 개발하였으며, 공개된 대형 언어 모델(LLM)의 성능을 평가했습니다. LLaMA-3.1, Gemma-2 등 5개의 오픈소스 LLM을 다양한 설정에서 평가한 결과, LLaMA 3.1이 일관된 성능을 보여 실용적인 Javadoc 자동 생성에 적합한 대안임을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 현대 자바 코드베이스에서 중요한 구조적 및 의미적 정보를 포함하는 새로운 Javadoc 생성용 데이터셋을 제시합니다.

- 2. 공개된 대형 언어 모델(LLMs)을 사용하여 문맥 인식 템플릿 기반 Javadoc 생성을 평가합니다.

- 3. LLaMA 3.1 모델은 실용적이고 자동화된 Javadoc 생성에 있어 일관된 성능을 보이며, 상용 시스템에 대한 유효한 대안이 될 수 있음을 입증했습니다.

- 4. 기존 자동화 접근법은 주로 코드 요약에 중점을 두었으며, 템플릿 기반 문서 생성에 대한 연구가 부족했습니다.

- 5. 본 연구는 현대 언어 기능을 포함하고 광범위한 프레임워크/라이브러리 범위를 제공하는 Javadoc 전용 데이터셋의 필요성을 강조합니다.

---

*Generated on 2025-09-19 16:39:48*