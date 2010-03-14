#!/usr/bin/perl
use strict;
use DBI;
my $dbname="geodjango";
my $username="geo";
my $password="12345";
my $host="localhost";
my $db = DBI->connect( "dbi:Pg:dbname=$dbname;host=$host",$username,$password,{RaiseError => 0, PrintError => 0,ShowErrorStatement => 1} ) ;

my $file = shift;
open (FILE,"<$file");

while (<FILE>)
{
	my $linea = $_;
	chomp $linea;
	my ($fecha,$sec,$x,$y,$error) = split (',',$linea);
	#print "($fecha,$sec,$x,$y,$error)\n";
	my $sql = "insert into rayos_rayos_ukmo (lon,lat,fecha,error,geopunto) values ($x,$y,'$fecha',$error,ST_GeomFromText('POINT($y $x)', 4326))";
	my $numfilas=$db->do($sql);
	if ($numfilas == 0)
	{
		if ($db->errstr =~ m/duplicate key/)
		{
			#print STDERR "ERROR EXISTEN daTOs $sql\n";
		}
		else
		{
			print STDERR "ERROR GRAVE:\n$sql\n".$db->errstr."\n";
		}
	}
	else
	{
		print "$sql\n";
	}

}

$db->disconnect();

