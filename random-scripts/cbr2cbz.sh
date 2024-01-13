#!/bin/bash
#
# Scrip originally taken from https://gist.githubusercontent.com/jaredlt/eef3ce973b6040f06396976314e9be60/raw/705862b3da032f83fba506bfe2e2681b7ccace85/cbr2cbz.sh
# Script has been modified to work under termux (unrar switches and tmp folder were change)
#
# Bulk convert cbr files to cbz
# Will recursively convert all cbr files for the provided path
#
# - Maintains exact file structure within archive
# - Defaults compression level to 'store' (no compression) as most compression already done in the images
#
# Requirements: `sudo apt install unar zip`
#
# Ensure this file is executable: `chmod +x cbr2cbz.sh`
#
# Usage:
# - Place this file 'cbr2cbz.sh' in your file system
# - From the command line, navigate to the directory where you placed it
# - Run using `./cbr2cbz.sh /full/path/to/files/`
# - IMPORTANT: Must use full path, if unsure, navigate to the directory
#   you want to convert and type `pwd` (that's the full path)
# - If you run `./cbr2cbz.sh` without a path parameter it will use the
#   the current working directory
#
# By default it will leave all original cbr files in place
# Uncomment the 'trash' line below to delete them after successful conversion
# NB. Tested on my own collection but there could still be some edge cases.
# Suggest testing on a small sample first.
#
# Troubleshooting
# - Receiving error: `touch: setting times of '/path/to/file.cbz': Operation not permitted`?
#   Run `sudo ./cbr2cbz.sh /full/path/to/files/` as your user may not have permissions to update the file


set -e # exit on error

# If no directory is specified, then use the current working directory (".").
if test -z "$1"; then
   SOURCEDIR=`pwd`
else
   SOURCEDIR="$1"
fi

echo "Using $SOURCEDIR"

echo "Converting CBRs to CBZs"

# Use RAM disk for temporary files.
WORKDIR="/data/data/com.termux/files/home/tmp"

# Separate files using ␜ http://graphemica.com/%E2%90%9C.
# Otherwise it will break on whitespace
# Could use IFS=$'\n' but it's a little more fragile
IFS="␜"

for INFILE in `find "$SOURCEDIR" -iname "*.cbr" -printf "%p␜"`; do
    # Absolute path to old file
    OLDFILE=`realpath "${INFILE}"`

    # Get the file name without the extension
    BASENAME=`basename "${OLDFILE%.*}"`

    # Path for the file. The ".zip" file will be written there.
    DIRNAME=`dirname "$OLDFILE"`

    # Name of the .zip file
    NEWNAME="${DIRNAME}/$BASENAME.cbz"

    if [ ! -e "${NEWNAME}" ]; then
        # Set name for the temp dir. This directory will be created under WORKDIR
        TEMPDIR=`mktemp -p "$WORKDIR" -d`

        # Create a temporary folder for unRARed files
        echo "Extracting $OLDFILE"

        # extract rar to temp directory
        unrar e "$OLDFILE" "${TEMPDIR}/"

        # move into temp directory to ensure zip archive matches exactly the original
        cd $TEMPDIR

        # Zip the files with no compression (store)
        zip -Z store -r "$NEWNAME" .

        # Preserve file modification time
        touch -r "$OLDFILE" "$NEWNAME"

        # Delete the temporary directory
        rm -r "$TEMPDIR"

        # OPTIONAL. Safe-remove the old file
        # gio trash "$OLDFILE"
    else
        echo "${NEWNAME}: File exists!"
    fi
done

echo "Conversion Done"
