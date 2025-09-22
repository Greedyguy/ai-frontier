# Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective

**Korean Title:** 분산 학습의 효율성 특성화: 전력, 성능 및 열 관점

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Compute-Communication Overlap|Compute-Communication Overlap]] [[keywords/specific/Activation Recomputation|Activation Recomputation]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Distributed Training|Distributed Training]] [[keywords/unique/CharLLM-PPT|CharLLM-PPT]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (84.9% similar) [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (84.1% similar) [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Compute-Communication Overlap
**🔗 Specific Connectable**: Parallelism Strategies
**🔬 Broad Technical**: Large Language Models, Distributed Training
**⭐ Unique Technical**: CharLLM-PPT
## 🔗 유사한 논문
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (84.9% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (84.1% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (83.6% similar)
- [[2025-09-19/{lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{lambda}Scale Enabling Fast Scaling for Serverless Large Language Model Inference]] (83.5% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (83.0% similar)


**ArXiv ID**: [2509.10371](https://arxiv.org/abs/2509.10371)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.10371.pdf)


**ArXiv ID**: [2509.10371](https://arxiv.org/abs/2509.10371)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.10371.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Parallelism Strategies
**🔗 Specific Connectable**: Activation Recomputation, Compute-Communication Overlap
**🔬 Broad Technical**: Large Language Models, Distributed Training

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Distributed Training` • 

`Activation Recomputation` • 

`Compute-Communication Overlap` • 

`Parallelism Strategies`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10371v2 Announce Type: replace-cross 
Abstract: The rapid scaling of Large Language Models (LLMs) has pushed training workloads far beyond the limits of single-node analysis, demanding a deeper understanding of how these models behave across large-scale, multi-GPU systems. In this paper, we present a comprehensive characterization of LLM training across diverse real-world workloads and hardware platforms, including NVIDIA H100/H200 and AMD MI250 GPUs. We analyze dense and sparse models under various parallelism strategies -- tensor, pipeline, data, and expert -- and evaluate their effects on hardware utilization, power consumption, and thermal behavior. We further evaluate the effectiveness of optimizations such as activation recomputation and compute-communication overlap. Our findings show that performance is not determined solely by scaling hardware capacity. Scale-up systems with fewer, higher-memory GPUs can outperform scale-out systems in communication-bound regimes, but only under carefully tuned configurations; in other cases, scale-out deployments achieve superior throughput. We also show that certain parallelism combinations, such as tensor with pipeline, lead to bandwidth underutilization due to inefficient data chunking, while increasing microbatch sizes beyond a certain point induces bursty execution and peak power excursions that worsen thermal throttling. These insights reveal how training performance is shaped by complex interactions between hardware, system topology, and model execution. We conclude by offering recommendations for system and hardware design to improve the scalability and reliability of future LLM systems and workloads. The source code of this project is available at https://github.com/sitar-lab/CharLLM-PPT.

## 🔍 Abstract (한글 번역)

arXiv:2509.10371v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)의 급속한 확장은 단일 노드 분석의 한계를 훨씬 넘어서는 훈련 작업을 요구하며, 이러한 모델이 대규모, 다중 GPU 시스템에서 어떻게 작동하는지에 대한 깊은 이해가 필요합니다. 본 논문에서는 NVIDIA H100/H200 및 AMD MI250 GPU를 포함한 다양한 실제 작업 부하와 하드웨어 플랫폼에서 LLM 훈련의 포괄적인 특성을 제시합니다. 우리는 텐서, 파이프라인, 데이터, 전문가 등 다양한 병렬 처리 전략 하에서 밀집 및 희소 모델을 분석하고, 하드웨어 활용도, 전력 소비 및 열적 행동에 미치는 영향을 평가합니다. 또한 활성화 재계산 및 계산-통신 중첩과 같은 최적화의 효과를 평가합니다. 우리의 연구 결과는 성능이 단순히 하드웨어 용량의 확장에 의해 결정되지 않음을 보여줍니다. 메모리가 더 많은 GPU가 적은 스케일 업 시스템은 통신에 제약이 있는 환경에서 스케일 아웃 시스템보다 뛰어난 성능을 발휘할 수 있지만, 이는 신중하게 조정된 구성에서만 가능합니다. 다른 경우에는 스케일 아웃 배포가 더 높은 처리량을 달성합니다. 또한 텐서와 파이프라인과 같은 특정 병렬 처리 조합이 비효율적인 데이터 청킹으로 인해 대역폭 활용도를 저하시킨다는 것을 보여주며, 마이크로 배치 크기를 특정 지점 이상으로 증가시키면 버스트 실행과 피크 전력 급증을 유발하여 열 스로틀링을 악화시킵니다. 이러한 통찰력은 하드웨어, 시스템 토폴로지 및 모델 실행 간의 복잡한 상호작용에 의해 훈련 성능이 어떻게 형성되는지를 드러냅니다. 우리는 미래의 LLM 시스템과 작업 부하의 확장성과 신뢰성을 개선하기 위한 시스템 및 하드웨어 설계에 대한 권장 사항을 제시하며 결론을 맺습니다. 이 프로젝트의 소스 코드는 https://github.com/sitar-lab/CharLLM-PPT에서 확인할 수 있습니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 훈련을 다양한 실제 작업과 하드웨어 플랫폼(NVIDIA H100/H200, AMD MI250 GPU 포함)에서 분석합니다. 밀집 및 희소 모델을 다양한 병렬화 전략(텐서, 파이프라인, 데이터, 전문가) 하에 평가하여 하드웨어 활용도, 전력 소비, 열적 특성에 미치는 영향을 조사합니다. 활성화 재계산 및 계산-통신 중첩과 같은 최적화의 효과도 평가합니다. 주요 발견은 하드웨어 용량의 확장이 성능을 결정하지 않으며, 고메모리 GPU를 사용하는 스케일업 시스템이 통신에 제약이 있는 상황에서 더 나은 성능을 발휘할 수 있다는 점입니다. 그러나 이는 세심한 조정이 필요하며, 그렇지 않으면 스케일아웃 배치가 더 높은 처리량을 달성합니다. 또한, 특정 병렬화 조합은 대역폭 활용을 저해하고, 마이크로배치 크기의 과도한 증가는 열 스로틀링을 악화시킵니다. 이러한 결과는 하드웨어, 시스템 토폴로지, 모델 실행 간의 복잡한 상호작용이 훈련 성능에 미치는 영향을 보여줍니다. 마지막으로, 향후 LLM 시스템과 작업의 확장성과 신뢰성을 개선하기 위한 시스템 및 하드웨어 설계에 대한 권장 사항을 제시합니다.

## 🎯 주요 포인트


- 1. 대규모 언어 모델(LLM) 훈련은 단일 노드 분석의 한계를 넘어 다중 GPU 시스템에서의 모델 동작 이해가 필요하다.

- 2. 다양한 병렬화 전략(텐서, 파이프라인, 데이터, 전문가)을 통해 하드웨어 활용, 전력 소비, 열적 특성을 평가하였다.

- 3. 하드웨어 용량의 확장만으로 성능이 결정되지 않으며, 적절히 조정된 구성에서 소수의 고용량 GPU를 사용하는 시스템이 더 나은 성능을 발휘할 수 있다.

- 4. 특정 병렬화 조합은 대역폭 활용을 저해하며, 마이크로배치 크기의 과도한 증가는 열 스로틀링을 악화시킬 수 있다.

- 5. 하드웨어, 시스템 토폴로지, 모델 실행 간의 복잡한 상호작용이 훈련 성능에 영향을 미친다.


---

*Generated on 2025-09-22 16:16:22*