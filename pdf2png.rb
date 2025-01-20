class Pdf2png < Formula
  desc "A quick script to convert PDFs to PNGs"
  homepage "https://github.com/varunaditya-plus/pdf2png"
  url "https://github.com/varunaditya-plus/pdf2png/archive/refs/tags/v0.2.0.tar.gz"
  sha256 "bef5b072e2888cafc21e1885e61bbb3c13ca34597bdfcade90a139cd88d02e08"
  license "MIT"

  depends_on "python@3.12"
  depends_on "poppler"

  include Language::Python::Virtualenv

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/pdf2png", "--help"
  end
end
