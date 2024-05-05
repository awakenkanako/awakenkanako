#! /usr/bin/perl

# ↑ 윗부분 Perl경로 확인합니다．

# 
# ----------------------------------------------------------
# Tiny Counter v1.0

# 오늘, 어제, 전체를 표시하고 페이지 뷰를 나타내는 기본적인 카운터 소스 입니다. 

# 아래 저작권을 명시한 상태에서 자유롭게 사용·개조·재 배포 가능합니다.
# 개조판을 재 배포한 때는 반드시 ，오리지널을 첨부한 상태로 배포하십시요.

#	- 연락처: Tiny@tinydesign.net
#	- 저작권: http://Tinydesign.net

# ----------------------------------------------------------
#        TinyDesign.net (c) 2000 by Tiny




# 안녕하세요. 타이니 입니다... 
# 아래 주석처리된 수정사항을 꼼꼼히 보시고 설치하시기 바랍니다.


 # --------------------------
 # 기본설정 부분

 # ----------------------------------------------------------------
 # 메인 데이터 파일의 지정．
 # 데이터 파일의 퍼미션을 666으로 지정해 주십시요.
 #
 # $DataFile = './tiny.dat'; 

 $DataFile = './tiny.dat';

 # ----------------------------------------------------------------
 # gifcat.pl 파일의 경로를 지정
 #
 # $GifcatPL = './gifcat.pl';

 $Gifcat = './gifcat.pl';

 # ----------------------------------------------------------------
 # 파일 록을 사용할지 안할지를 지정합니다.
 # 록 기능을 이용해서 카운터가 리셋되는것을 막습니다.
 #
 # $UseFileLock = 1; # 파일 록을 사용한다．
 # $UseFileLock = 0; # 파일 록을 사용하지 않는다．(리셋될 가능성이 있습니다)

 $UseFileLock = 1;
#$UseFileLock = 0;

 # ----------------------------------------------------------------
 # 지정 시간내의 중복 액세스를 무시할지를 정합니다.
 # 리로드나 브라우저의 BACK 버튼 등으로 ２ 회 카운트한 것을 막습니다．
 #
 # $UseCookLock = 0; # 중복 카운트 허용
 # $UseCookLock = 1; # 중복 카운트 불가

 $UseCookLock = 1;

 # ----------------------------------------------------------------
 # 쿠키의 유효기한 지정．
 # 얼마만큼의 시간동안 중복 액세스를 무시할지를 정합니다.
 # 지정한 시간내에는 2차례 페이지를 표시해도 카운트 되지 않습니다．
 # 단,  앞의 설정으로 cookie기능을 막았을때는 소용없습니다.
 #
 # $CookLimit = 60*60*2;   # ２시간 지정한 경우 (60x60x2[초] = ２시 간 )

 $CookLimit = 10*60*1;

 # ----------------------------------------------------------------
 # 쿠키 이름의 설정．서버내에 cookie를 사용한 다른 cgi와의 충돌을 피합니다.
 # 중복되는 것을 방지하기 위해 사용．특별히 변경할 필요없음．
 #
 # $CookNameHead = 'tiny_';

 $CookNameHead = 'tiny_';

 # ----------------------------------------------------------------
 # 쿠키의 값의 설정．가능한한 알파벳과 숫자+[_]로 지정．
 #
 # $CookValue = 'tinycnt';

 $CookValue = 'tinycnt';

 # ----------------------------------------------------------------
 # 디폴트 이미지 폴더를 설정합니다.
 # 마지막에 '/'로 끝나는 것을 주의해 주세요．
 # html문서내에 삽입한 카운터태그에서 이미지 폴더를 지정해 주지 않았을경우 적용됩니다.
 # 
 # $DEF_ImgDir = 'dir/'

 $DEF_ImgDir = 'tiny3/';

 # ----------------------------------------------------------------
 # 이미지 폴더의 지정．옵션[type]로 지정한 문자열과 그 때에 사용된
 # 이미지 폴더의 대응표를 작성합니다．
 #
 # %ImgDir = (
 #     'name', 'dir/',
 #     'name', 'dir/',
 #     'name', 'dir/',
 # );

 %ImgDir = (
 	'tiny1',		'tiny1/', 
 	'tiny2',	'tiny2/', 
 	'tiny3',	'tiny3/', 
 	'tiny4',	'tiny4/', 
 	'tiny5',	'tiny5/', 

 	'tiny6',	'tiny6/', 
 );

 # ----------------------------------------------------------------
 # 디폴트 카운터 폭의 지정． [width]옵션이 없는 때에 적용
 # 단 실제의 카운트 수가 더 클경우，무시됩니다．
 #
 # $DEF_Width = 4; # 4 자릿수에 설정

 $DEF_Width = 1;

 # ----------------------------------------------------------------
 # 서버와의 시간차를 조정．취득한 시간을 수정합니다.
 # 이는 해외 서버에 설치하고 있을경우，국내 시간으로 표시하기 위해
 # 몇 시간을 늦추거나 빠르게 합니다．
 #
 # $TimeDiff = -60*60*8;

 $TimeDiff = 0;

 # ----------------------------------------------------------------
 # 카운터 표시 데이터 네임 변경．[mode]옵션으로 지정하는 값입니다.
 # 수정하실 필요가 없습니다.
 # 대문자 소문자는 구별하지 않습니다．
 # 
 # $KEY_default = 'main';        # 보통의 카운터를 표시하기 위한 키
 # $KEY_yeCount = 'prev';      # 어제의 카운트를 표시하기 위한 키
 # $KEY_toCount = 'today';     # 오늘의 카운트를 표시하기 위한 키

 $KEY_default = 'main';
 $KEY_yeCount = 'prev';
 $KEY_toCount = 'today';

 # ----------------------------------------------------------------
 # 초기화 항목 입니다．변경하시면 아니되옵니당 *^^*．

 $ImgDir{_DEFAULT_} = $DEF_ImgDir;
 $DEF_Width         = $DEF_Width   ||  1;


1;


 # ----------------------------------------------------------------


 $Build = 'v1.0';


 # 옵션의 취득
 &GetOption;
 &ChkOption;

 &ChkImgDir($Type);

 $Mode  = '' if( $Mode ne $KEY_toCount && $Mode ne $KEY_yeCount );

 # 쿠키 록
 if(!$Mode && $UseCookLock ){
 	 &ChkCook( $CookNameHead.$Name, $CookValue );
 	 &SetCook( $CookNameHead.$Name, $CookValue, $CookLimit ) if(!$CookLock);
 }

 # 데이터 취득

 if(!$Mode && !$CookLock ){ &getValue($Name,'incr'); }
 else                     { &getValue($Name);        }

 $Count = $YeCnt   if( $Mode eq $KEY_yeCount );
 $Count = $ToCnt   if( $Mode eq $KEY_toCount );
 $Count = $MainCnt if(!$Mode                 );

 # 출력．
 &putCounter( $Count,$Width,$Type);


# putImg.pl
#---------------



sub putCounter{

	#---------------------
	# 카운터 이미지 출력

	local($Count,$Width,$Type) = @_;
	local(@ImgPath,$Number);

	eval{ require $Gifcat; };
	if( $@ ){ &Err("gifcat.pl 파일을 읽어 드릴수가 없습니다.($@)"); }

	$Width  = length($Count) if( $Width < length($Count) );
	$ImgDir = $ImgDir{$Type};

	foreach(1..$Width){
		$Number = substr( $Count, -$_, 1);
		$Number = '0' if(!$Number);
		unshift( @ImgPath, "$ImgDir$Number.gif");
	}

	binmode(STDOUT);
	print "Content-type: image/gif\n";
	print "Expires: 01/01/70 00:00:00 GMT\n\n";
	print &gifcat'gifcat(@ImgPath);
	exit;


}


1;

# ioData.pl
#---------------


sub getValue{

# ---------------------------------
# ToXxxx는 오늘의 카운트     [To]day..
# YeXxxx는 어제의 카운트     [Ye]sterday
# 
#

	local($Date,$OldDate,$SaveFlag);
	local($Name,$Mode) = (@_);

	$ToDate = &getToDate;
	$YeDate = &getYeDate;

	open( FH, "+<$DataFile" ) || &Err("데이터 파일을 열수 없습니다.($DataFile: $!)");
		&Lock; @Data = <FH>;

	for(@Data){
		if( /^$Name\t/ ){
			($Name,$MainCnt,$ToCnt,$YeCnt,$OldDate) = split(/\t/,$_);
			$OldDate =~ s/\n$//; $_ = '';
			last;
		}
	}

	if(!$MainCnt){
		$MainCnt = 0;	$SaveFlag = 1;
		$ToCnt   = 0;	$YeCnt    = 0;
		$OldDate = $ToDate;
	}

	if( $OldDate != $ToDate && $OldDate == $YeDate ){ $YeCnt = $ToCnt; $ToCnt = 0; $SaveFlag = 1; }
	if( $OldDate != $ToDate && $OldDate != $YeDate ){ $YeCnt =      0; $ToCnt = 0; $SaveFlag = 1; }

	if( $Mode eq 'incr' ){
		$MainCnt++;
		$ToCnt++;
		$SaveFlag = 1;
	}

	push( @Data, "$Name\t$MainCnt\t$ToCnt\t$YeCnt\t$ToDate\n");

	if( $SaveFlag ){
		seek(FH,0,0);
		truncate(FH,0);
		print FH @Data;
		close(FH);
	}
}

1;

# output.pl
#---------------

sub Err{ &PutMsg('에러가 발생했습니다．', "·@_"); }

sub PutMsg{ 

	#---------------------
	# 에러 출력．

	$Title= shift(@_);

	print "Content-type: text/html\n\n";
	print "<HTML>\n";
	print "<b> $Title </b>\n<ul>";
	print @_;
	print "</ul>\n";

	print "<div align=right>\n".
	      "<hr><a href=http://www.Tinydesign.net/> Tiny Counter $Build</a><br>\n".
	      "TinyDesign.net (c) 2000 By Tiny.</div>";

	print "</HTML>";
	exit;

}

1;
# dircheck.pl
#---------------


sub ChkImgDir{

	local($Type) = shift(@_);

	&Err("이미지 디렉토리가 존재하지 않습니다.($ImgDir{$Type})") if( !-e $ImgDir{$Type} );

	for( 0..9 ){
		&Err("${_}.gif가 없습니다．($ImgDir{$Type}${_}.gif)") if( !-e "$ImgDir{$Type}"."${_}.gif" );
	}

}

1;


# lock.pl
#---------------

sub Lock{

	#---------------------
	# 록 처리．

	return if(!$UseFileLock);

	eval{ flock(FH,2); };
	&Err('록에 실패했습니다．이 상황이 계속된 경우는 「$UseFileLock = 0;」으로 지정하십시오．'."( $@ )") if( $@ );

}

1;

# cook.pl
#---------------

sub SetCook{

	#---------------------
	# cookie의 출력

	local( $Name,$Value,$Limit ) = @_;

	local($date);
	local($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time + $Limit);

	 $year = sprintf( "%04d", $year + 1900 ); # 2000년 문제 대응
	 $sec  = sprintf( "%02d", $sec  ); $min  = sprintf( "%02d", $min  );
	 $hour = sprintf( "%02d", $hour ); $mday = sprintf( "%02d", $mday );

	 $wday = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') [$wday];
	 $mon  = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mon];
	 $date = "$wday, $mday\-$mon\-$year $hour:$min:$sec GMT";

	print "Set-Cookie: $Name=$Value; expires=$date\n";
}

sub ChkCook{

	local($Cook);
	local($CookName,$CookValue) = @_;

	$Cook =  $ENV{'HTTP_COOKIE'};
	$Cook =~ s/; /;/g;

	@CookPart = split( /;/,$Cook );

	for( @CookPart ){
		if(/^$CookName=$CookValue$/){
			$CookLock = 1; return 1;
		}
	}

	return 0;

}

1;


# decode.pl
#---------------

sub GetOption{

	#---------------------
	# 인수 취득

	$buffer = $ENV{'QUERY_STRING'};

	foreach( split(/&/,$buffer) ){
		($name,$value) = split(/=/);
		 $name  =~ tr/[A-Z]/[a-z]/;
		 $value =~ s/\t/    /g;
		 $OPT{$name} = $value;
	}

	$Name  = $OPT{'name'}  || 'default';
	$Type  = $OPT{'type'}  || '_DEFAULT_';
	$Mode  = $OPT{'mode'}  || $KEY_default;
	$Width = $OPT{'width'} || $DEF_Width;

}

sub ChkOption{

	local($br) = '<br><font color=red>';
	local($ft) = '</font>';

#	&Err("type의 값이 부정확 합니다  ( type  = $Type  ) $br →지정한 수치를 벗어나지는 않았나요?  $ft"               ) if( $Type  =~ /\D/      );
	&Err("width의 값이 부정확 합니다 ( width = $Width ) $br →지정한 수치를 벗어나지는 않았나요?  $ft"               ) if( $Width =~ /\D/      );
	&Err("name의 값이 부정확 합니다  ( name  = $Name  ) $br → (, ), [, ], |, ^, \\, \$ 은  카운터 이름에 사용할 수 없습니다．$ft") if( $Name  =~ /[\(\)\[\]\|\^\\\$]/ );
	&Err("name의 값이 부정확 합니다  ( name  = $Name  ) $br →이 카운터 이름으로는  정상적으로 카운트업할 수 없습니다．  $ft") if( $Name  !~ /^$Name$/ );

	&Err("이미지 폴더(\$ImgDir{$Type})가 설정되어 있지 않습니다．"                                         ) if(!$ImgDir{$Type}       );

}


1;

# getDate.pl
#---------------


sub getDate{

	local( $Diff ) = shift(@_); # 취득한 일자의 지정(오늘/어제)

	local($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time + $TimeDiff + $Diff );

	 $year = sprintf( "%02d", $year + 1900 ); # 2000년 문제 대응
	 $mon  = sprintf( "%02d", $mon+1 );
	 $mday = sprintf( "%02d", $mday );

	return $year.$mon.$mday;

}

sub getToDate{ return &getDate( 0 );         }
sub getYeDate{ return &getDate( -60*60*24 ); }


1;
