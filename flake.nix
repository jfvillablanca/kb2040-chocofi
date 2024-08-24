{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    devenv.url = "github:cachix/devenv";
  };

  outputs = {
    self,
    nixpkgs,
    devenv,
    flake-utils,
    ...
  } @ inputs:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
      mpy-cross =
        pkgs.stdenv.mkDerivation
        {
          name = "mpy-cross";
          src = pkgs.fetchurl {
            url = "https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/linux-amd64/mpy-cross-linux-amd64-9.1.1.static";
            hash = "sha256-i865idypRM/7HYMWg80zLTc/mztzdDjycuFH1Y1JkcY=";
          };

          phases = ["installPhase"];

          installPhase = ''
            runHook preInstall

            mkdir -p $out/bin
            cp $src $out/bin/mpy-cross
            chmod +x $out/bin/mpy-cross

            runHook postInstall
          '';

          meta.mainProgram = "mpy-cross";
        };
    in {
      devShells.default = devenv.lib.mkShell {
        inherit inputs pkgs;
        modules = [
          {
            name = "work";
            languages = {
              nix.enable = true;
            };
            packages = with pkgs;
              [
                alejandra
                just
              ]
              ++ (with pkgs.python3Packages; [
                python-lsp-server
                pylint
                mypy
              ])
              ++ [
                mpy-cross
              ];
            env = {
              NIX_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
                pkgs.stdenv.cc.cc
                pkgs.openssl
                # ...
              ];
              NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";
            };
          }
        ];
      };
    });
}
