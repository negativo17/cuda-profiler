%global real_name cuda_profiler_api

%global debug_package %{nil}
%global major_package_version 13-1

Name:           cuda-profiler
Epoch:          1
Version:        13.1.115
Release:        1%{?dist}
Summary:        CUDA Profiler API
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
BuildArch:      noarch

# Different tarballs per architecture but they all contain the same headers:
Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz

%description
NVIDIA CUDA API for profiling.

%package devel
Summary:        Development files for CUDA Profiler API
Conflicts:      %{real_name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA Profiler API.

%prep
%autosetup -n %{real_name}-linux-x86_64-%{version}-archive

%install
mkdir -p %{buildroot}%{_includedir}
cp -f include/* %{buildroot}%{_includedir}/

%files devel
%license LICENSE
%{_includedir}/*

%changelog
* Mon Feb 02 2026 Simone Caronni <negativo17@gmail.com> - 1:13.1.115-1
- Update to 13.1.115.

* Sun Dec 07 2025 Simone Caronni <negativo17@gmail.com> - 1:13.0.85-1
- Update to 13.0.85.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.53-1
- Update to 12.2.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.105-1
- Update to 12.1.105.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.55-1
- Update to 12.1.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.140-1
- Update to 12.0.140.

* Wed Dec 21 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.76-1
- Update to 12.0.76.

* Wed Dec 21 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.86-1
- First build for 11.8.86.
