#! /usr/bin/perl

# �� ���κ� Perl��� Ȯ���մϴ٣�

# 
# ----------------------------------------------------------
# Tiny Counter v1.0

# ����, ����, ��ü�� ǥ���ϰ� ������ �並 ��Ÿ���� �⺻���� ī���� �ҽ� �Դϴ�. 

# �Ʒ� ���۱��� ����� ���¿��� �����Ӱ� ��롤�������� ���� �����մϴ�.
# �������� �� ������ ���� �ݵ�� ������������ ÷���� ���·� �����Ͻʽÿ�.

#	- ����ó: Tiny@tinydesign.net
#	- ���۱�: http://Tinydesign.net

# ----------------------------------------------------------
#        TinyDesign.net (c) 2000 by Tiny




# �ȳ��ϼ���. Ÿ�̴� �Դϴ�... 
# �Ʒ� �ּ�ó���� ���������� �Ĳ��� ���ð� ��ġ�Ͻñ� �ٶ��ϴ�.


 # --------------------------
 # �⺻���� �κ�

 # ----------------------------------------------------------------
 # ���� ������ ������ ������
 # ������ ������ �۹̼��� 666���� ������ �ֽʽÿ�.
 #
 # $DataFile = './tiny.dat'; 

 $DataFile = './tiny.dat';

 # ----------------------------------------------------------------
 # gifcat.pl ������ ��θ� ����
 #
 # $GifcatPL = './gifcat.pl';

 $Gifcat = './gifcat.pl';

 # ----------------------------------------------------------------
 # ���� ���� ������� �������� �����մϴ�.
 # �� ����� �̿��ؼ� ī���Ͱ� ���µǴ°��� �����ϴ�.
 #
 # $UseFileLock = 1; # ���� ���� ����Ѵ٣�
 # $UseFileLock = 0; # ���� ���� ������� �ʴ´٣�(���µ� ���ɼ��� �ֽ��ϴ�)

 $UseFileLock = 1;
#$UseFileLock = 0;

 # ----------------------------------------------------------------
 # ���� �ð����� �ߺ� �׼����� ���������� ���մϴ�.
 # ���ε峪 �������� BACK ��ư ������ �� ȸ ī��Ʈ�� ���� �����ϴ٣�
 #
 # $UseCookLock = 0; # �ߺ� ī��Ʈ ���
 # $UseCookLock = 1; # �ߺ� ī��Ʈ �Ұ�

 $UseCookLock = 1;

 # ----------------------------------------------------------------
 # ��Ű�� ��ȿ���� ������
 # �󸶸�ŭ�� �ð����� �ߺ� �׼����� ���������� ���մϴ�.
 # ������ �ð������� 2���� �������� ǥ���ص� ī��Ʈ ���� �ʽ��ϴ٣�
 # ��,  ���� �������� cookie����� ���������� �ҿ�����ϴ�.
 #
 # $CookLimit = 60*60*2;   # ���ð� ������ ��� (60x60x2[��] = ���� �� )

 $CookLimit = 10*60*1;

 # ----------------------------------------------------------------
 # ��Ű �̸��� �������������� cookie�� ����� �ٸ� cgi���� �浹�� ���մϴ�.
 # �ߺ��Ǵ� ���� �����ϱ� ���� ��룮Ư���� ������ �ʿ������
 #
 # $CookNameHead = 'tiny_';

 $CookNameHead = 'tiny_';

 # ----------------------------------------------------------------
 # ��Ű�� ���� �������������� ���ĺ��� ����+[_]�� ������
 #
 # $CookValue = 'tinycnt';

 $CookValue = 'tinycnt';

 # ----------------------------------------------------------------
 # ����Ʈ �̹��� ������ �����մϴ�.
 # �������� '/'�� ������ ���� ������ �ּ��䣮
 # html�������� ������ ī�����±׿��� �̹��� ������ ������ ���� �ʾ������ ����˴ϴ�.
 # 
 # $DEF_ImgDir = 'dir/'

 $DEF_ImgDir = 'tiny3/';

 # ----------------------------------------------------------------
 # �̹��� ������ �������ɼ�[type]�� ������ ���ڿ��� �� ���� ����
 # �̹��� ������ ����ǥ�� �ۼ��մϴ٣�
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
 # ����Ʈ ī���� ���� ������ [width]�ɼ��� ���� ���� ����
 # �� ������ ī��Ʈ ���� �� Ŭ��죬���õ˴ϴ٣�
 #
 # $DEF_Width = 4; # 4 �ڸ����� ����

 $DEF_Width = 1;

 # ----------------------------------------------------------------
 # �������� �ð����� ����������� �ð��� �����մϴ�.
 # �̴� �ؿ� ������ ��ġ�ϰ� ������죬���� �ð����� ǥ���ϱ� ����
 # �� �ð��� ���߰ų� ������ �մϴ٣�
 #
 # $TimeDiff = -60*60*8;

 $TimeDiff = 0;

 # ----------------------------------------------------------------
 # ī���� ǥ�� ������ ���� ���森[mode]�ɼ����� �����ϴ� ���Դϴ�.
 # �����Ͻ� �ʿ䰡 �����ϴ�.
 # �빮�� �ҹ��ڴ� �������� �ʽ��ϴ٣�
 # 
 # $KEY_default = 'main';        # ������ ī���͸� ǥ���ϱ� ���� Ű
 # $KEY_yeCount = 'prev';      # ������ ī��Ʈ�� ǥ���ϱ� ���� Ű
 # $KEY_toCount = 'today';     # ������ ī��Ʈ�� ǥ���ϱ� ���� Ű

 $KEY_default = 'main';
 $KEY_yeCount = 'prev';
 $KEY_toCount = 'today';

 # ----------------------------------------------------------------
 # �ʱ�ȭ �׸� �Դϴ٣������Ͻø� �ƴϵǿɴϴ� *^^*��

 $ImgDir{_DEFAULT_} = $DEF_ImgDir;
 $DEF_Width         = $DEF_Width   ||  1;


1;


 # ----------------------------------------------------------------


 $Build = 'v1.0';


 # �ɼ��� ���
 &GetOption;
 &ChkOption;

 &ChkImgDir($Type);

 $Mode  = '' if( $Mode ne $KEY_toCount && $Mode ne $KEY_yeCount );

 # ��Ű ��
 if(!$Mode && $UseCookLock ){
 	 &ChkCook( $CookNameHead.$Name, $CookValue );
 	 &SetCook( $CookNameHead.$Name, $CookValue, $CookLimit ) if(!$CookLock);
 }

 # ������ ���

 if(!$Mode && !$CookLock ){ &getValue($Name,'incr'); }
 else                     { &getValue($Name);        }

 $Count = $YeCnt   if( $Mode eq $KEY_yeCount );
 $Count = $ToCnt   if( $Mode eq $KEY_toCount );
 $Count = $MainCnt if(!$Mode                 );

 # ��£�
 &putCounter( $Count,$Width,$Type);


# putImg.pl
#---------------



sub putCounter{

	#---------------------
	# ī���� �̹��� ���

	local($Count,$Width,$Type) = @_;
	local(@ImgPath,$Number);

	eval{ require $Gifcat; };
	if( $@ ){ &Err("gifcat.pl ������ �о� �帱���� �����ϴ�.($@)"); }

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
# ToXxxx�� ������ ī��Ʈ     [To]day..
# YeXxxx�� ������ ī��Ʈ     [Ye]sterday
# 
#

	local($Date,$OldDate,$SaveFlag);
	local($Name,$Mode) = (@_);

	$ToDate = &getToDate;
	$YeDate = &getYeDate;

	open( FH, "+<$DataFile" ) || &Err("������ ������ ���� �����ϴ�.($DataFile: $!)");
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

sub Err{ &PutMsg('������ �߻��߽��ϴ٣�', "��@_"); }

sub PutMsg{ 

	#---------------------
	# ���� ��£�

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

	&Err("�̹��� ���丮�� �������� �ʽ��ϴ�.($ImgDir{$Type})") if( !-e $ImgDir{$Type} );

	for( 0..9 ){
		&Err("${_}.gif�� �����ϴ٣�($ImgDir{$Type}${_}.gif)") if( !-e "$ImgDir{$Type}"."${_}.gif" );
	}

}

1;


# lock.pl
#---------------

sub Lock{

	#---------------------
	# �� ó����

	return if(!$UseFileLock);

	eval{ flock(FH,2); };
	&Err('�Ͽ� �����߽��ϴ٣��� ��Ȳ�� ��ӵ� ���� ��$UseFileLock = 0;������ �����Ͻʽÿ���'."( $@ )") if( $@ );

}

1;

# cook.pl
#---------------

sub SetCook{

	#---------------------
	# cookie�� ���

	local( $Name,$Value,$Limit ) = @_;

	local($date);
	local($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime(time + $Limit);

	 $year = sprintf( "%04d", $year + 1900 ); # 2000�� ���� ����
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
	# �μ� ���

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

#	&Err("type�� ���� ����Ȯ �մϴ�  ( type  = $Type  ) $br �������� ��ġ�� ������� �ʾҳ���?  $ft"               ) if( $Type  =~ /\D/      );
	&Err("width�� ���� ����Ȯ �մϴ� ( width = $Width ) $br �������� ��ġ�� ������� �ʾҳ���?  $ft"               ) if( $Width =~ /\D/      );
	&Err("name�� ���� ����Ȯ �մϴ�  ( name  = $Name  ) $br �� (, ), [, ], |, ^, \\, \$ ��  ī���� �̸��� ����� �� �����ϴ٣�$ft") if( $Name  =~ /[\(\)\[\]\|\^\\\$]/ );
	&Err("name�� ���� ����Ȯ �մϴ�  ( name  = $Name  ) $br ���� ī���� �̸����δ�  ���������� ī��Ʈ���� �� �����ϴ٣�  $ft") if( $Name  !~ /^$Name$/ );

	&Err("�̹��� ����(\$ImgDir{$Type})�� �����Ǿ� ���� �ʽ��ϴ٣�"                                         ) if(!$ImgDir{$Type}       );

}


1;

# getDate.pl
#---------------


sub getDate{

	local( $Diff ) = shift(@_); # ����� ������ ����(����/����)

	local($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time + $TimeDiff + $Diff );

	 $year = sprintf( "%02d", $year + 1900 ); # 2000�� ���� ����
	 $mon  = sprintf( "%02d", $mon+1 );
	 $mday = sprintf( "%02d", $mday );

	return $year.$mon.$mday;

}

sub getToDate{ return &getDate( 0 );         }
sub getYeDate{ return &getDate( -60*60*24 ); }


1;
