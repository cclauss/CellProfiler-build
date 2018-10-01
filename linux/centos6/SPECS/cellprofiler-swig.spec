%define pkgname cellprofiler-swig
%define version 2.0.1
%define release 1
%define tarname swig
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   swig
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   GPLv2+ and LGPLv2+ and BSD
URL:       http://www.swig.org/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  pcre cellprofiler-python
BuildRequires: pcre-devel cellprofiler-python gcc gcc-c++

%description
swig installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

./configure \
 --prefix="%{pref}" \
 --with-python="%{pref}/bin/python" \
 --without-python3

make


%install

make install DESTDIR=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/ccache-swig
%{pref}/bin/swig
%{pref}/share/man/man1/ccache-swig.1
%{pref}/share/swig/2.0.1/allegrocl/allegrocl.swg
%{pref}/share/swig/2.0.1/allegrocl/inout_typemaps.i
%{pref}/share/swig/2.0.1/allegrocl/longlongs.i
%{pref}/share/swig/2.0.1/allegrocl/std_list.i
%{pref}/share/swig/2.0.1/allegrocl/std_string.i
%{pref}/share/swig/2.0.1/allegrocl/typemaps.i
%{pref}/share/swig/2.0.1/allkw.swg
%{pref}/share/swig/2.0.1/attribute.i
%{pref}/share/swig/2.0.1/carrays.i
%{pref}/share/swig/2.0.1/cdata.i
%{pref}/share/swig/2.0.1/cffi/cffi.swg
%{pref}/share/swig/2.0.1/chicken/chicken.swg
%{pref}/share/swig/2.0.1/chicken/chickenkw.swg
%{pref}/share/swig/2.0.1/chicken/chickenrun.swg
%{pref}/share/swig/2.0.1/chicken/multi-generic.scm
%{pref}/share/swig/2.0.1/chicken/std_string.i
%{pref}/share/swig/2.0.1/chicken/swigclosprefix.scm
%{pref}/share/swig/2.0.1/chicken/tinyclos-multi-generic.patch
%{pref}/share/swig/2.0.1/chicken/typemaps.i
%{pref}/share/swig/2.0.1/clisp/clisp.swg
%{pref}/share/swig/2.0.1/cmalloc.i
%{pref}/share/swig/2.0.1/constraints.i
%{pref}/share/swig/2.0.1/cpointer.i
%{pref}/share/swig/2.0.1/csharp/arrays_csharp.i
%{pref}/share/swig/2.0.1/csharp/boost_shared_ptr.i
%{pref}/share/swig/2.0.1/csharp/csharp.swg
%{pref}/share/swig/2.0.1/csharp/csharphead.swg
%{pref}/share/swig/2.0.1/csharp/csharpkw.swg
%{pref}/share/swig/2.0.1/csharp/director.swg
%{pref}/share/swig/2.0.1/csharp/enums.swg
%{pref}/share/swig/2.0.1/csharp/enumsimple.swg
%{pref}/share/swig/2.0.1/csharp/enumtypesafe.swg
%{pref}/share/swig/2.0.1/csharp/std_common.i
%{pref}/share/swig/2.0.1/csharp/std_deque.i
%{pref}/share/swig/2.0.1/csharp/std_except.i
%{pref}/share/swig/2.0.1/csharp/std_map.i
%{pref}/share/swig/2.0.1/csharp/std_pair.i
%{pref}/share/swig/2.0.1/csharp/std_shared_ptr.i
%{pref}/share/swig/2.0.1/csharp/std_string.i
%{pref}/share/swig/2.0.1/csharp/std_vector.i
%{pref}/share/swig/2.0.1/csharp/std_wstring.i
%{pref}/share/swig/2.0.1/csharp/stl.i
%{pref}/share/swig/2.0.1/csharp/typemaps.i
%{pref}/share/swig/2.0.1/csharp/wchar.i
%{pref}/share/swig/2.0.1/cstring.i
%{pref}/share/swig/2.0.1/cwstring.i
%{pref}/share/swig/2.0.1/exception.i
%{pref}/share/swig/2.0.1/gcj/cni.i
%{pref}/share/swig/2.0.1/gcj/cni.swg
%{pref}/share/swig/2.0.1/gcj/javaprims.i
%{pref}/share/swig/2.0.1/go/cdata.i
%{pref}/share/swig/2.0.1/go/exception.i
%{pref}/share/swig/2.0.1/go/go.swg
%{pref}/share/swig/2.0.1/go/gokw.swg
%{pref}/share/swig/2.0.1/go/goruntime.swg
%{pref}/share/swig/2.0.1/go/std_common.i
%{pref}/share/swig/2.0.1/go/std_deque.i
%{pref}/share/swig/2.0.1/go/std_except.i
%{pref}/share/swig/2.0.1/go/std_map.i
%{pref}/share/swig/2.0.1/go/std_pair.i
%{pref}/share/swig/2.0.1/go/std_string.i
%{pref}/share/swig/2.0.1/go/std_vector.i
%{pref}/share/swig/2.0.1/go/stl.i
%{pref}/share/swig/2.0.1/go/typemaps.i
%{pref}/share/swig/2.0.1/guile/common.scm
%{pref}/share/swig/2.0.1/guile/cplusplus.i
%{pref}/share/swig/2.0.1/guile/ghinterface.i
%{pref}/share/swig/2.0.1/guile/guile.i
%{pref}/share/swig/2.0.1/guile/guile_gh.swg
%{pref}/share/swig/2.0.1/guile/guile_gh_run.swg
%{pref}/share/swig/2.0.1/guile/guile_scm.swg
%{pref}/share/swig/2.0.1/guile/guile_scm_run.swg
%{pref}/share/swig/2.0.1/guile/guilemain.i
%{pref}/share/swig/2.0.1/guile/interpreter.i
%{pref}/share/swig/2.0.1/guile/list-vector.i
%{pref}/share/swig/2.0.1/guile/pointer-in-out.i
%{pref}/share/swig/2.0.1/guile/ports.i
%{pref}/share/swig/2.0.1/guile/std_common.i
%{pref}/share/swig/2.0.1/guile/std_deque.i
%{pref}/share/swig/2.0.1/guile/std_except.i
%{pref}/share/swig/2.0.1/guile/std_map.i
%{pref}/share/swig/2.0.1/guile/std_pair.i
%{pref}/share/swig/2.0.1/guile/std_string.i
%{pref}/share/swig/2.0.1/guile/std_vector.i
%{pref}/share/swig/2.0.1/guile/stl.i
%{pref}/share/swig/2.0.1/guile/swigrun.i
%{pref}/share/swig/2.0.1/guile/typemaps.i
%{pref}/share/swig/2.0.1/intrusive_ptr.i
%{pref}/share/swig/2.0.1/inttypes.i
%{pref}/share/swig/2.0.1/java/arrays_java.i
%{pref}/share/swig/2.0.1/java/boost_intrusive_ptr.i
%{pref}/share/swig/2.0.1/java/boost_shared_ptr.i
%{pref}/share/swig/2.0.1/java/director.swg
%{pref}/share/swig/2.0.1/java/enums.swg
%{pref}/share/swig/2.0.1/java/enumsimple.swg
%{pref}/share/swig/2.0.1/java/enumtypesafe.swg
%{pref}/share/swig/2.0.1/java/enumtypeunsafe.swg
%{pref}/share/swig/2.0.1/java/java.swg
%{pref}/share/swig/2.0.1/java/javahead.swg
%{pref}/share/swig/2.0.1/java/javakw.swg
%{pref}/share/swig/2.0.1/java/std_common.i
%{pref}/share/swig/2.0.1/java/std_deque.i
%{pref}/share/swig/2.0.1/java/std_except.i
%{pref}/share/swig/2.0.1/java/std_map.i
%{pref}/share/swig/2.0.1/java/std_pair.i
%{pref}/share/swig/2.0.1/java/std_shared_ptr.i
%{pref}/share/swig/2.0.1/java/std_string.i
%{pref}/share/swig/2.0.1/java/std_vector.i
%{pref}/share/swig/2.0.1/java/std_wstring.i
%{pref}/share/swig/2.0.1/java/stl.i
%{pref}/share/swig/2.0.1/java/typemaps.i
%{pref}/share/swig/2.0.1/java/various.i
%{pref}/share/swig/2.0.1/lua/_std_common.i
%{pref}/share/swig/2.0.1/lua/carrays.i
%{pref}/share/swig/2.0.1/lua/lua.swg
%{pref}/share/swig/2.0.1/lua/lua_fnptr.i
%{pref}/share/swig/2.0.1/lua/luarun.swg
%{pref}/share/swig/2.0.1/lua/luaruntime.swg
%{pref}/share/swig/2.0.1/lua/luatypemaps.swg
%{pref}/share/swig/2.0.1/lua/std_common.i
%{pref}/share/swig/2.0.1/lua/std_deque.i
%{pref}/share/swig/2.0.1/lua/std_except.i
%{pref}/share/swig/2.0.1/lua/std_map.i
%{pref}/share/swig/2.0.1/lua/std_pair.i
%{pref}/share/swig/2.0.1/lua/std_string.i
%{pref}/share/swig/2.0.1/lua/std_vector.i
%{pref}/share/swig/2.0.1/lua/stl.i
%{pref}/share/swig/2.0.1/lua/typemaps.i
%{pref}/share/swig/2.0.1/lua/wchar.i
%{pref}/share/swig/2.0.1/math.i
%{pref}/share/swig/2.0.1/modula3/modula3.swg
%{pref}/share/swig/2.0.1/modula3/modula3head.swg
%{pref}/share/swig/2.0.1/modula3/typemaps.i
%{pref}/share/swig/2.0.1/mzscheme/mzrun.swg
%{pref}/share/swig/2.0.1/mzscheme/mzscheme.swg
%{pref}/share/swig/2.0.1/mzscheme/std_common.i
%{pref}/share/swig/2.0.1/mzscheme/std_deque.i
%{pref}/share/swig/2.0.1/mzscheme/std_map.i
%{pref}/share/swig/2.0.1/mzscheme/std_pair.i
%{pref}/share/swig/2.0.1/mzscheme/std_string.i
%{pref}/share/swig/2.0.1/mzscheme/std_vector.i
%{pref}/share/swig/2.0.1/mzscheme/stl.i
%{pref}/share/swig/2.0.1/mzscheme/typemaps.i
%{pref}/share/swig/2.0.1/ocaml/carray.i
%{pref}/share/swig/2.0.1/ocaml/class.swg
%{pref}/share/swig/2.0.1/ocaml/cstring.i
%{pref}/share/swig/2.0.1/ocaml/director.swg
%{pref}/share/swig/2.0.1/ocaml/ocaml.i
%{pref}/share/swig/2.0.1/ocaml/ocaml.swg
%{pref}/share/swig/2.0.1/ocaml/ocamldec.swg
%{pref}/share/swig/2.0.1/ocaml/ocamlkw.swg
%{pref}/share/swig/2.0.1/ocaml/preamble.swg
%{pref}/share/swig/2.0.1/ocaml/std_common.i
%{pref}/share/swig/2.0.1/ocaml/std_complex.i
%{pref}/share/swig/2.0.1/ocaml/std_deque.i
%{pref}/share/swig/2.0.1/ocaml/std_list.i
%{pref}/share/swig/2.0.1/ocaml/std_map.i
%{pref}/share/swig/2.0.1/ocaml/std_pair.i
%{pref}/share/swig/2.0.1/ocaml/std_string.i
%{pref}/share/swig/2.0.1/ocaml/std_vector.i
%{pref}/share/swig/2.0.1/ocaml/stl.i
%{pref}/share/swig/2.0.1/ocaml/swig.ml
%{pref}/share/swig/2.0.1/ocaml/swig.mli
%{pref}/share/swig/2.0.1/ocaml/swigp4.ml
%{pref}/share/swig/2.0.1/ocaml/typecheck.i
%{pref}/share/swig/2.0.1/ocaml/typemaps.i
%{pref}/share/swig/2.0.1/ocaml/typeregister.swg
%{pref}/share/swig/2.0.1/octave/attribute.i
%{pref}/share/swig/2.0.1/octave/boost_shared_ptr.i
%{pref}/share/swig/2.0.1/octave/carrays.i
%{pref}/share/swig/2.0.1/octave/cdata.i
%{pref}/share/swig/2.0.1/octave/cmalloc.i
%{pref}/share/swig/2.0.1/octave/director.swg
%{pref}/share/swig/2.0.1/octave/exception.i
%{pref}/share/swig/2.0.1/octave/factory.i
%{pref}/share/swig/2.0.1/octave/implicit.i
%{pref}/share/swig/2.0.1/octave/octave.swg
%{pref}/share/swig/2.0.1/octave/octcomplex.swg
%{pref}/share/swig/2.0.1/octave/octcontainer.swg
%{pref}/share/swig/2.0.1/octave/octfragments.swg
%{pref}/share/swig/2.0.1/octave/octiterators.swg
%{pref}/share/swig/2.0.1/octave/octopers.swg
%{pref}/share/swig/2.0.1/octave/octprimtypes.swg
%{pref}/share/swig/2.0.1/octave/octrun.swg
%{pref}/share/swig/2.0.1/octave/octruntime.swg
%{pref}/share/swig/2.0.1/octave/octstdcommon.swg
%{pref}/share/swig/2.0.1/octave/octtypemaps.swg
%{pref}/share/swig/2.0.1/octave/octuserdir.swg
%{pref}/share/swig/2.0.1/octave/std_alloc.i
%{pref}/share/swig/2.0.1/octave/std_basic_string.i
%{pref}/share/swig/2.0.1/octave/std_carray.i
%{pref}/share/swig/2.0.1/octave/std_char_traits.i
%{pref}/share/swig/2.0.1/octave/std_common.i
%{pref}/share/swig/2.0.1/octave/std_complex.i
%{pref}/share/swig/2.0.1/octave/std_container.i
%{pref}/share/swig/2.0.1/octave/std_deque.i
%{pref}/share/swig/2.0.1/octave/std_except.i
%{pref}/share/swig/2.0.1/octave/std_map.i
%{pref}/share/swig/2.0.1/octave/std_pair.i
%{pref}/share/swig/2.0.1/octave/std_string.i
%{pref}/share/swig/2.0.1/octave/std_vector.i
%{pref}/share/swig/2.0.1/octave/stl.i
%{pref}/share/swig/2.0.1/octave/typemaps.i
%{pref}/share/swig/2.0.1/perl5/Makefile.pl
%{pref}/share/swig/2.0.1/perl5/attribute.i
%{pref}/share/swig/2.0.1/perl5/carrays.i
%{pref}/share/swig/2.0.1/perl5/cdata.i
%{pref}/share/swig/2.0.1/perl5/cmalloc.i
%{pref}/share/swig/2.0.1/perl5/cni.i
%{pref}/share/swig/2.0.1/perl5/cpointer.i
%{pref}/share/swig/2.0.1/perl5/cstring.i
%{pref}/share/swig/2.0.1/perl5/exception.i
%{pref}/share/swig/2.0.1/perl5/factory.i
%{pref}/share/swig/2.0.1/perl5/jstring.i
%{pref}/share/swig/2.0.1/perl5/noembed.h
%{pref}/share/swig/2.0.1/perl5/perl5.swg
%{pref}/share/swig/2.0.1/perl5/perlerrors.swg
%{pref}/share/swig/2.0.1/perl5/perlfragments.swg
%{pref}/share/swig/2.0.1/perl5/perlhead.swg
%{pref}/share/swig/2.0.1/perl5/perlinit.swg
%{pref}/share/swig/2.0.1/perl5/perlkw.swg
%{pref}/share/swig/2.0.1/perl5/perlmacros.swg
%{pref}/share/swig/2.0.1/perl5/perlmain.i
%{pref}/share/swig/2.0.1/perl5/perlopers.swg
%{pref}/share/swig/2.0.1/perl5/perlprimtypes.swg
%{pref}/share/swig/2.0.1/perl5/perlrun.swg
%{pref}/share/swig/2.0.1/perl5/perlruntime.swg
%{pref}/share/swig/2.0.1/perl5/perlstrings.swg
%{pref}/share/swig/2.0.1/perl5/perltypemaps.swg
%{pref}/share/swig/2.0.1/perl5/perluserdir.swg
%{pref}/share/swig/2.0.1/perl5/reference.i
%{pref}/share/swig/2.0.1/perl5/std_common.i
%{pref}/share/swig/2.0.1/perl5/std_deque.i
%{pref}/share/swig/2.0.1/perl5/std_except.i
%{pref}/share/swig/2.0.1/perl5/std_list.i
%{pref}/share/swig/2.0.1/perl5/std_map.i
%{pref}/share/swig/2.0.1/perl5/std_pair.i
%{pref}/share/swig/2.0.1/perl5/std_string.i
%{pref}/share/swig/2.0.1/perl5/std_vector.i
%{pref}/share/swig/2.0.1/perl5/stl.i
%{pref}/share/swig/2.0.1/perl5/typemaps.i
%{pref}/share/swig/2.0.1/php/const.i
%{pref}/share/swig/2.0.1/php/director.swg
%{pref}/share/swig/2.0.1/php/factory.i
%{pref}/share/swig/2.0.1/php/globalvar.i
%{pref}/share/swig/2.0.1/php/php.swg
%{pref}/share/swig/2.0.1/php/phpinit.swg
%{pref}/share/swig/2.0.1/php/phpkw.swg
%{pref}/share/swig/2.0.1/php/phppointers.i
%{pref}/share/swig/2.0.1/php/phprun.swg
%{pref}/share/swig/2.0.1/php/std_common.i
%{pref}/share/swig/2.0.1/php/std_deque.i
%{pref}/share/swig/2.0.1/php/std_map.i
%{pref}/share/swig/2.0.1/php/std_pair.i
%{pref}/share/swig/2.0.1/php/std_string.i
%{pref}/share/swig/2.0.1/php/std_vector.i
%{pref}/share/swig/2.0.1/php/stl.i
%{pref}/share/swig/2.0.1/php/typemaps.i
%{pref}/share/swig/2.0.1/php/utils.i
%{pref}/share/swig/2.0.1/pike/pike.swg
%{pref}/share/swig/2.0.1/pike/pikekw.swg
%{pref}/share/swig/2.0.1/pike/pikerun.swg
%{pref}/share/swig/2.0.1/pike/std_string.i
%{pref}/share/swig/2.0.1/pointer.i
%{pref}/share/swig/2.0.1/python/argcargv.i
%{pref}/share/swig/2.0.1/python/attribute.i
%{pref}/share/swig/2.0.1/python/boost_shared_ptr.i
%{pref}/share/swig/2.0.1/python/carrays.i
%{pref}/share/swig/2.0.1/python/ccomplex.i
%{pref}/share/swig/2.0.1/python/cdata.i
%{pref}/share/swig/2.0.1/python/cmalloc.i
%{pref}/share/swig/2.0.1/python/cni.i
%{pref}/share/swig/2.0.1/python/complex.i
%{pref}/share/swig/2.0.1/python/cpointer.i
%{pref}/share/swig/2.0.1/python/cstring.i
%{pref}/share/swig/2.0.1/python/cwstring.i
%{pref}/share/swig/2.0.1/python/defarg.swg
%{pref}/share/swig/2.0.1/python/director.swg
%{pref}/share/swig/2.0.1/python/embed.i
%{pref}/share/swig/2.0.1/python/embed15.i
%{pref}/share/swig/2.0.1/python/exception.i
%{pref}/share/swig/2.0.1/python/factory.i
%{pref}/share/swig/2.0.1/python/file.i
%{pref}/share/swig/2.0.1/python/implicit.i
%{pref}/share/swig/2.0.1/python/jstring.i
%{pref}/share/swig/2.0.1/python/pyabc.i
%{pref}/share/swig/2.0.1/python/pyapi.swg
%{pref}/share/swig/2.0.1/python/pybackward.swg
%{pref}/share/swig/2.0.1/python/pybuffer.i
%{pref}/share/swig/2.0.1/python/pyclasses.swg
%{pref}/share/swig/2.0.1/python/pycomplex.swg
%{pref}/share/swig/2.0.1/python/pycontainer.swg
%{pref}/share/swig/2.0.1/python/pydocs.swg
%{pref}/share/swig/2.0.1/python/pyerrors.swg
%{pref}/share/swig/2.0.1/python/pyfragments.swg
%{pref}/share/swig/2.0.1/python/pyhead.swg
%{pref}/share/swig/2.0.1/python/pyinit.swg
%{pref}/share/swig/2.0.1/python/pyiterators.swg
%{pref}/share/swig/2.0.1/python/pymacros.swg
%{pref}/share/swig/2.0.1/python/pyname_compat.i
%{pref}/share/swig/2.0.1/python/pyopers.swg
%{pref}/share/swig/2.0.1/python/pyprimtypes.swg
%{pref}/share/swig/2.0.1/python/pyrun.swg
%{pref}/share/swig/2.0.1/python/pyruntime.swg
%{pref}/share/swig/2.0.1/python/pystdcommon.swg
%{pref}/share/swig/2.0.1/python/pystrings.swg
%{pref}/share/swig/2.0.1/python/python.swg
%{pref}/share/swig/2.0.1/python/pythonkw.swg
%{pref}/share/swig/2.0.1/python/pythreads.swg
%{pref}/share/swig/2.0.1/python/pytuplehlp.swg
%{pref}/share/swig/2.0.1/python/pytypemaps.swg
%{pref}/share/swig/2.0.1/python/pyuserdir.swg
%{pref}/share/swig/2.0.1/python/pywstrings.swg
%{pref}/share/swig/2.0.1/python/std_alloc.i
%{pref}/share/swig/2.0.1/python/std_basic_string.i
%{pref}/share/swig/2.0.1/python/std_carray.i
%{pref}/share/swig/2.0.1/python/std_char_traits.i
%{pref}/share/swig/2.0.1/python/std_common.i
%{pref}/share/swig/2.0.1/python/std_complex.i
%{pref}/share/swig/2.0.1/python/std_container.i
%{pref}/share/swig/2.0.1/python/std_deque.i
%{pref}/share/swig/2.0.1/python/std_except.i
%{pref}/share/swig/2.0.1/python/std_ios.i
%{pref}/share/swig/2.0.1/python/std_iostream.i
%{pref}/share/swig/2.0.1/python/std_list.i
%{pref}/share/swig/2.0.1/python/std_map.i
%{pref}/share/swig/2.0.1/python/std_multimap.i
%{pref}/share/swig/2.0.1/python/std_multiset.i
%{pref}/share/swig/2.0.1/python/std_pair.i
%{pref}/share/swig/2.0.1/python/std_set.i
%{pref}/share/swig/2.0.1/python/std_shared_ptr.i
%{pref}/share/swig/2.0.1/python/std_sstream.i
%{pref}/share/swig/2.0.1/python/std_streambuf.i
%{pref}/share/swig/2.0.1/python/std_string.i
%{pref}/share/swig/2.0.1/python/std_vector.i
%{pref}/share/swig/2.0.1/python/std_vectora.i
%{pref}/share/swig/2.0.1/python/std_wios.i
%{pref}/share/swig/2.0.1/python/std_wiostream.i
%{pref}/share/swig/2.0.1/python/std_wsstream.i
%{pref}/share/swig/2.0.1/python/std_wstreambuf.i
%{pref}/share/swig/2.0.1/python/std_wstring.i
%{pref}/share/swig/2.0.1/python/stl.i
%{pref}/share/swig/2.0.1/python/typemaps.i
%{pref}/share/swig/2.0.1/python/wchar.i
%{pref}/share/swig/2.0.1/r/cdata.i
%{pref}/share/swig/2.0.1/r/exception.i
%{pref}/share/swig/2.0.1/r/r.swg
%{pref}/share/swig/2.0.1/r/rcontainer.swg
%{pref}/share/swig/2.0.1/r/rfragments.swg
%{pref}/share/swig/2.0.1/r/rkw.swg
%{pref}/share/swig/2.0.1/r/ropers.swg
%{pref}/share/swig/2.0.1/r/rrun.swg
%{pref}/share/swig/2.0.1/r/rstdcommon.swg
%{pref}/share/swig/2.0.1/r/rtype.swg
%{pref}/share/swig/2.0.1/r/srun.swg
%{pref}/share/swig/2.0.1/r/std_alloc.i
%{pref}/share/swig/2.0.1/r/std_common.i
%{pref}/share/swig/2.0.1/r/std_container.i
%{pref}/share/swig/2.0.1/r/std_deque.i
%{pref}/share/swig/2.0.1/r/std_except.i
%{pref}/share/swig/2.0.1/r/std_map.i
%{pref}/share/swig/2.0.1/r/std_pair.i
%{pref}/share/swig/2.0.1/r/std_string.i
%{pref}/share/swig/2.0.1/r/std_vector.i
%{pref}/share/swig/2.0.1/r/stl.i
%{pref}/share/swig/2.0.1/r/typemaps.i
%{pref}/share/swig/2.0.1/ruby/Makefile.swig
%{pref}/share/swig/2.0.1/ruby/argcargv.i
%{pref}/share/swig/2.0.1/ruby/attribute.i
%{pref}/share/swig/2.0.1/ruby/carrays.i
%{pref}/share/swig/2.0.1/ruby/cdata.i
%{pref}/share/swig/2.0.1/ruby/cmalloc.i
%{pref}/share/swig/2.0.1/ruby/cni.i
%{pref}/share/swig/2.0.1/ruby/cpointer.i
%{pref}/share/swig/2.0.1/ruby/cstring.i
%{pref}/share/swig/2.0.1/ruby/director.swg
%{pref}/share/swig/2.0.1/ruby/embed.i
%{pref}/share/swig/2.0.1/ruby/exception.i
%{pref}/share/swig/2.0.1/ruby/extconf.rb
%{pref}/share/swig/2.0.1/ruby/factory.i
%{pref}/share/swig/2.0.1/ruby/file.i
%{pref}/share/swig/2.0.1/ruby/jstring.i
%{pref}/share/swig/2.0.1/ruby/progargcargv.i
%{pref}/share/swig/2.0.1/ruby/ruby.swg
%{pref}/share/swig/2.0.1/ruby/rubyapi.swg
%{pref}/share/swig/2.0.1/ruby/rubyautodoc.swg
%{pref}/share/swig/2.0.1/ruby/rubyclasses.swg
%{pref}/share/swig/2.0.1/ruby/rubycomplex.swg
%{pref}/share/swig/2.0.1/ruby/rubycontainer.swg
%{pref}/share/swig/2.0.1/ruby/rubycontainer_extended.swg
%{pref}/share/swig/2.0.1/ruby/rubydef.swg
%{pref}/share/swig/2.0.1/ruby/rubyerrors.swg
%{pref}/share/swig/2.0.1/ruby/rubyfragments.swg
%{pref}/share/swig/2.0.1/ruby/rubyhead.swg
%{pref}/share/swig/2.0.1/ruby/rubyinit.swg
%{pref}/share/swig/2.0.1/ruby/rubyiterators.swg
%{pref}/share/swig/2.0.1/ruby/rubykw.swg
%{pref}/share/swig/2.0.1/ruby/rubymacros.swg
%{pref}/share/swig/2.0.1/ruby/rubyopers.swg
%{pref}/share/swig/2.0.1/ruby/rubyprimtypes.swg
%{pref}/share/swig/2.0.1/ruby/rubyrun.swg
%{pref}/share/swig/2.0.1/ruby/rubyruntime.swg
%{pref}/share/swig/2.0.1/ruby/rubystdautodoc.swg
%{pref}/share/swig/2.0.1/ruby/rubystdcommon.swg
%{pref}/share/swig/2.0.1/ruby/rubystdfunctors.swg
%{pref}/share/swig/2.0.1/ruby/rubystrings.swg
%{pref}/share/swig/2.0.1/ruby/rubytracking.swg
%{pref}/share/swig/2.0.1/ruby/rubytypemaps.swg
%{pref}/share/swig/2.0.1/ruby/rubyuserdir.swg
%{pref}/share/swig/2.0.1/ruby/rubywstrings.swg
%{pref}/share/swig/2.0.1/ruby/std_alloc.i
%{pref}/share/swig/2.0.1/ruby/std_basic_string.i
%{pref}/share/swig/2.0.1/ruby/std_char_traits.i
%{pref}/share/swig/2.0.1/ruby/std_common.i
%{pref}/share/swig/2.0.1/ruby/std_complex.i
%{pref}/share/swig/2.0.1/ruby/std_container.i
%{pref}/share/swig/2.0.1/ruby/std_deque.i
%{pref}/share/swig/2.0.1/ruby/std_except.i
%{pref}/share/swig/2.0.1/ruby/std_functors.i
%{pref}/share/swig/2.0.1/ruby/std_ios.i
%{pref}/share/swig/2.0.1/ruby/std_iostream.i
%{pref}/share/swig/2.0.1/ruby/std_list.i
%{pref}/share/swig/2.0.1/ruby/std_map.i
%{pref}/share/swig/2.0.1/ruby/std_multimap.i
%{pref}/share/swig/2.0.1/ruby/std_multiset.i
%{pref}/share/swig/2.0.1/ruby/std_pair.i
%{pref}/share/swig/2.0.1/ruby/std_queue.i
%{pref}/share/swig/2.0.1/ruby/std_set.i
%{pref}/share/swig/2.0.1/ruby/std_sstream.i
%{pref}/share/swig/2.0.1/ruby/std_stack.i
%{pref}/share/swig/2.0.1/ruby/std_streambuf.i
%{pref}/share/swig/2.0.1/ruby/std_string.i
%{pref}/share/swig/2.0.1/ruby/std_vector.i
%{pref}/share/swig/2.0.1/ruby/std_vectora.i
%{pref}/share/swig/2.0.1/ruby/std_wstring.i
%{pref}/share/swig/2.0.1/ruby/stl.i
%{pref}/share/swig/2.0.1/ruby/timeval.i
%{pref}/share/swig/2.0.1/ruby/typemaps.i
%{pref}/share/swig/2.0.1/runtime.swg
%{pref}/share/swig/2.0.1/shared_ptr.i
%{pref}/share/swig/2.0.1/std/_std_deque.i
%{pref}/share/swig/2.0.1/std/std_alloc.i
%{pref}/share/swig/2.0.1/std/std_basic_string.i
%{pref}/share/swig/2.0.1/std/std_carray.swg
%{pref}/share/swig/2.0.1/std/std_char_traits.i
%{pref}/share/swig/2.0.1/std/std_common.i
%{pref}/share/swig/2.0.1/std/std_container.i
%{pref}/share/swig/2.0.1/std/std_deque.i
%{pref}/share/swig/2.0.1/std/std_except.i
%{pref}/share/swig/2.0.1/std/std_ios.i
%{pref}/share/swig/2.0.1/std/std_iostream.i
%{pref}/share/swig/2.0.1/std/std_list.i
%{pref}/share/swig/2.0.1/std/std_map.i
%{pref}/share/swig/2.0.1/std/std_multimap.i
%{pref}/share/swig/2.0.1/std/std_multiset.i
%{pref}/share/swig/2.0.1/std/std_pair.i
%{pref}/share/swig/2.0.1/std/std_queue.i
%{pref}/share/swig/2.0.1/std/std_set.i
%{pref}/share/swig/2.0.1/std/std_sstream.i
%{pref}/share/swig/2.0.1/std/std_stack.i
%{pref}/share/swig/2.0.1/std/std_streambuf.i
%{pref}/share/swig/2.0.1/std/std_string.i
%{pref}/share/swig/2.0.1/std/std_vector.i
%{pref}/share/swig/2.0.1/std/std_vectora.i
%{pref}/share/swig/2.0.1/std/std_wios.i
%{pref}/share/swig/2.0.1/std/std_wiostream.i
%{pref}/share/swig/2.0.1/std/std_wsstream.i
%{pref}/share/swig/2.0.1/std/std_wstreambuf.i
%{pref}/share/swig/2.0.1/std/std_wstring.i
%{pref}/share/swig/2.0.1/std_except.i
%{pref}/share/swig/2.0.1/stdint.i
%{pref}/share/swig/2.0.1/stl.i
%{pref}/share/swig/2.0.1/swig.swg
%{pref}/share/swig/2.0.1/swigarch.i
%{pref}/share/swig/2.0.1/swigerrors.swg
%{pref}/share/swig/2.0.1/swiginit.swg
%{pref}/share/swig/2.0.1/swiglabels.swg
%{pref}/share/swig/2.0.1/swigrun.i
%{pref}/share/swig/2.0.1/swigrun.swg
%{pref}/share/swig/2.0.1/swigwarn.swg
%{pref}/share/swig/2.0.1/swigwarnings.swg
%{pref}/share/swig/2.0.1/tcl/attribute.i
%{pref}/share/swig/2.0.1/tcl/carrays.i
%{pref}/share/swig/2.0.1/tcl/cdata.i
%{pref}/share/swig/2.0.1/tcl/cmalloc.i
%{pref}/share/swig/2.0.1/tcl/cni.i
%{pref}/share/swig/2.0.1/tcl/cpointer.i
%{pref}/share/swig/2.0.1/tcl/cstring.i
%{pref}/share/swig/2.0.1/tcl/cwstring.i
%{pref}/share/swig/2.0.1/tcl/exception.i
%{pref}/share/swig/2.0.1/tcl/factory.i
%{pref}/share/swig/2.0.1/tcl/jstring.i
%{pref}/share/swig/2.0.1/tcl/std_common.i
%{pref}/share/swig/2.0.1/tcl/std_deque.i
%{pref}/share/swig/2.0.1/tcl/std_except.i
%{pref}/share/swig/2.0.1/tcl/std_map.i
%{pref}/share/swig/2.0.1/tcl/std_pair.i
%{pref}/share/swig/2.0.1/tcl/std_string.i
%{pref}/share/swig/2.0.1/tcl/std_vector.i
%{pref}/share/swig/2.0.1/tcl/std_wstring.i
%{pref}/share/swig/2.0.1/tcl/stl.i
%{pref}/share/swig/2.0.1/tcl/tcl8.swg
%{pref}/share/swig/2.0.1/tcl/tclapi.swg
%{pref}/share/swig/2.0.1/tcl/tclerrors.swg
%{pref}/share/swig/2.0.1/tcl/tclfragments.swg
%{pref}/share/swig/2.0.1/tcl/tclinit.swg
%{pref}/share/swig/2.0.1/tcl/tclinterp.i
%{pref}/share/swig/2.0.1/tcl/tclkw.swg
%{pref}/share/swig/2.0.1/tcl/tclmacros.swg
%{pref}/share/swig/2.0.1/tcl/tclopers.swg
%{pref}/share/swig/2.0.1/tcl/tclprimtypes.swg
%{pref}/share/swig/2.0.1/tcl/tclresult.i
%{pref}/share/swig/2.0.1/tcl/tclrun.swg
%{pref}/share/swig/2.0.1/tcl/tclruntime.swg
%{pref}/share/swig/2.0.1/tcl/tclsh.i
%{pref}/share/swig/2.0.1/tcl/tclstrings.swg
%{pref}/share/swig/2.0.1/tcl/tcltypemaps.swg
%{pref}/share/swig/2.0.1/tcl/tcluserdir.swg
%{pref}/share/swig/2.0.1/tcl/tclwstrings.swg
%{pref}/share/swig/2.0.1/tcl/typemaps.i
%{pref}/share/swig/2.0.1/tcl/wish.i
%{pref}/share/swig/2.0.1/typemaps/attribute.swg
%{pref}/share/swig/2.0.1/typemaps/carrays.swg
%{pref}/share/swig/2.0.1/typemaps/cdata.swg
%{pref}/share/swig/2.0.1/typemaps/cmalloc.swg
%{pref}/share/swig/2.0.1/typemaps/cpointer.swg
%{pref}/share/swig/2.0.1/typemaps/cstring.swg
%{pref}/share/swig/2.0.1/typemaps/cstrings.swg
%{pref}/share/swig/2.0.1/typemaps/cwstring.swg
%{pref}/share/swig/2.0.1/typemaps/enumint.swg
%{pref}/share/swig/2.0.1/typemaps/exception.swg
%{pref}/share/swig/2.0.1/typemaps/factory.swg
%{pref}/share/swig/2.0.1/typemaps/fragments.swg
%{pref}/share/swig/2.0.1/typemaps/implicit.swg
%{pref}/share/swig/2.0.1/typemaps/inoutlist.swg
%{pref}/share/swig/2.0.1/typemaps/misctypes.swg
%{pref}/share/swig/2.0.1/typemaps/primtypes.swg
%{pref}/share/swig/2.0.1/typemaps/ptrtypes.swg
%{pref}/share/swig/2.0.1/typemaps/std_except.swg
%{pref}/share/swig/2.0.1/typemaps/std_string.swg
%{pref}/share/swig/2.0.1/typemaps/std_strings.swg
%{pref}/share/swig/2.0.1/typemaps/std_wstring.swg
%{pref}/share/swig/2.0.1/typemaps/string.swg
%{pref}/share/swig/2.0.1/typemaps/strings.swg
%{pref}/share/swig/2.0.1/typemaps/swigmacros.swg
%{pref}/share/swig/2.0.1/typemaps/swigobject.swg
%{pref}/share/swig/2.0.1/typemaps/swigtype.swg
%{pref}/share/swig/2.0.1/typemaps/swigtypemaps.swg
%{pref}/share/swig/2.0.1/typemaps/traits.swg
%{pref}/share/swig/2.0.1/typemaps/typemaps.swg
%{pref}/share/swig/2.0.1/typemaps/valtypes.swg
%{pref}/share/swig/2.0.1/typemaps/void.swg
%{pref}/share/swig/2.0.1/typemaps/wstring.swg
%{pref}/share/swig/2.0.1/uffi/uffi.swg
%{pref}/share/swig/2.0.1/wchar.i
%{pref}/share/swig/2.0.1/windows.i