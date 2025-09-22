# ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning

**Korean Title:** ConCISE: 단계별 효율적인 추론에서 신뢰도 기반 압축

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Confidence Guided Compression

## 🔗 유사한 논문
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (87.0% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression A Self-Optimizing Framework]] (86.9% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models A Perspective from Schoenfeld's Episode Theory]] (85.3% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE Faithful Logic-Aided Reasoning and Exploration]] (84.2% similar)
- [[2025-09-17/Slim-SC_ Thought Pruning for Efficient Scaling with Self-Consistency_20250917|Slim-SC Thought Pruning for Efficient Scaling with Self-Consistency]] (83.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.04881v2 Announce Type: replace-cross 
Abstract: Large Reasoning Models (LRMs) perform strongly in complex reasoning tasks via Chain-of-Thought (CoT) prompting, but often suffer from verbose outputs, increasing computational overhead. Existing fine-tuning-based compression methods either operate post-hoc pruning, risking disruption to reasoning coherence, or rely on sampling-based selection, which fails to remove redundant content thoroughly. To address these limitations, this work begins by framing two key patterns of redundant reflection in LRMs--Confidence Deficit, wherein the model reflects on correct intermediate steps, and Termination Delay, where reflection continues after a verified, confident answer--through a confidence-guided perspective. Based on this, we introduce ConCISE (Confidence-guided Compression In Step-by-step Efficient Reasoning), a framework designed to generate concise reasoning chains, integrating Confidence Injection to boost reasoning confidence, and Early Stopping to terminate reasoning when confidence is sufficient. Extensive experiments demonstrate that compared to baseline methods, fine-tuning LRMs on ConCISE-generated data yields a better balance between compression and task performance, reducing length by up to approximately 50% under SimPO, while maintaining high task accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2505.04881v2 발표 유형: 교차 교체  
초록: 대규모 추론 모델(LRMs)은 연쇄 사고(Chain-of-Thought, CoT) 유도를 통해 복잡한 추론 작업에서 강력한 성능을 발휘하지만, 종종 장황한 출력으로 인해 계산적 부담이 증가하는 문제가 있습니다. 기존의 미세 조정 기반 압축 방법은 사후 가지치기를 수행하여 추론의 일관성을 해칠 위험이 있거나, 샘플링 기반 선택에 의존하여 불필요한 내용을 철저히 제거하지 못합니다. 이러한 한계를 해결하기 위해, 본 연구는 LRMs에서의 두 가지 주요 중복 반영 패턴을 자신감 결핍(Confidence Deficit)과 종료 지연(Termination Delay)으로 정의합니다. 자신감 결핍은 모델이 올바른 중간 단계를 반영하는 경우를, 종료 지연은 확인된 자신감 있는 답변 이후에도 반영이 계속되는 경우를 의미합니다. 이를 기반으로, 우리는 자신감 유도 압축을 통한 단계별 효율적 추론(ConCISE)이라는 프레임워크를 도입하여, 추론 자신감을 높이기 위한 자신감 주입(Confidence Injection)과 충분한 자신감이 있을 때 추론을 종료하는 조기 종료(Early Stopping)를 통합하여 간결한 추론 체인을 생성합니다. 광범위한 실험 결과, ConCISE로 생성된 데이터로 LRMs을 미세 조정하면, 기존 방법에 비해 압축과 작업 성능 간의 균형이 개선되며, SimPO 하에서 길이를 약 50%까지 줄이면서도 높은 작업 정확도를 유지함을 보여줍니다.

## 📝 요약

이 논문은 대규모 추론 모델(LRMs)의 복잡한 추론 작업에서 발생하는 장황한 출력 문제를 해결하기 위해 ConCISE라는 새로운 프레임워크를 제안합니다. 기존의 압축 방법은 추론의 일관성을 해치거나 중복 내용을 완전히 제거하지 못하는 한계가 있습니다. ConCISE는 Confidence Injection과 Early Stopping을 통해 추론의 자신감을 높이고 불필요한 반영을 줄입니다. 실험 결과, ConCISE를 사용한 모델은 기존 방법에 비해 출력 길이를 최대 50% 줄이면서도 높은 정확도를 유지하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 대규모 추론 모델(LRMs)은 복잡한 추론 작업에서 강력한 성능을 보이지만, 장황한 출력으로 인해 계산적 부담이 증가하는 문제가 있다.

- 2. 기존의 압축 방법은 추론의 일관성을 해칠 위험이 있는 사후 가지치기나 중복 콘텐츠를 완전히 제거하지 못하는 샘플링 기반 선택에 의존한다.

- 3. 본 연구는 Confidence Deficit과 Termination Delay라는 두 가지 중복 반영 패턴을 식별하고, 이를 해결하기 위해 Confidence Injection과 Early Stopping을 통합한 ConCISE 프레임워크를 제안한다.

- 4. ConCISE는 추론의 자신감을 높이고, 충분한 자신감이 있을 때 추론을 조기에 종료하여 간결한 추론 체인을 생성한다.

- 5. 실험 결과, ConCISE를 사용한 미세 조정은 기존 방법에 비해 약 50%의 길이 감소와 높은 작업 정확성을 유지하며 압축과 작업 성능 간의 균형을 더 잘 맞춘다.

---

*Generated on 2025-09-22 14:46:55*