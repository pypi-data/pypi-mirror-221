#!/bin/bash

mkdir -p ${PAPI_DIR}
mkdir -p ${POLYBENCH_DIR}

tar -xzf ${BENCHMARK_DIR}/packages/papi701.tar.gz -C ${PAPI_DIR}
tar -xzf ${BENCHMARK_DIR}/packages/polybench.tar.gz -C ${POLYBENCH_DIR}

pushd ${PAPI_DIR}/src/src
./configure --prefix=${PAPI_DIR}
make && make install
popd

pushd ${POLYBENCH_DIR}/src
make
popd

rm -rf ${PAPI_DIR}/src
rm -rf ${POLYBENCH_DIR}/src

