### RPM cms cmssw-osenv 230704.0
## NOCOMPILER
## NO_VERSION_SUFFIX

# ***Do not change minor number of the above version. ***

%define commit 91dae8c41187daaf11cb130c92bf9252af168183
%define branch master
# We do not use a revision explicitly, because revisioned packages do not get
# updated automatically when there are dependencies.
%define fakerevision %(echo %realversion | cut -d. -f1)
Source0: git://github.com/cms-sw/cmssw-osenv.git?obj=%{branch}/%{commit}&export=cmssw-osenv&output=/cmssw-osenv-%{commit}.tgz

%prep
%setup -n %{n}

%build

%install
mkdir -p %{i}/common
mv * %{i}/common

%post
cd ${RPM_INSTALL_PREFIX}/%{pkgrel}
mkdir -p ${RPM_INSTALL_PREFIX}/common ${RPM_INSTALL_PREFIX}/etc/%{pkgname}

#Check if a newer revision is already installed
if [ -f ${RPM_INSTALL_PREFIX}/etc/%{pkgname}/version ] ; then
  oldrev=$(cat ${RPM_INSTALL_PREFIX}/etc/%{pkgname}/version )
  if [ ${oldrev} -ge %{fakerevision} ] ; then
    exit 0
  fi
fi

for file in $(find . -name '*' -type f -path '*/common/*') ; do
  cp -f ${file} ${RPM_INSTALL_PREFIX}/${file}
done
for file in $(find . -name '*' -type l -path '*/common/*') ; do
  cp -pRf ${file} ${RPM_INSTALL_PREFIX}/${file}
done

echo %{fakerevision} > ${RPM_INSTALL_PREFIX}/etc/%{pkgname}/version
