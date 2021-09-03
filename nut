/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  8
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      nut;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -1 0 0 0 0];

internalField   uniform 8.58e-06;

boundaryField
{
    inlet
    {
        type            freestream;
        freestreamValue uniform 8.58e-06;
    }

    outlet
    {
        type            freestream;
        freestreamValue uniform 8.58e-06;
    }

    airfoil
    {
        type            fixedValue;
        value           uniform 0;
    }

    frontandback
    {
        type            empty;
    }
}

// ************************************************************************* //
