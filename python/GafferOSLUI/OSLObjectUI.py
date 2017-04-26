##########################################################################
#
#  Copyright (c) 2013-2014, John Haddon. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import IECore
import Gaffer
import GafferUI

import GafferOSL

##########################################################################
# Metadata
##########################################################################

Gaffer.Metadata.registerNode(

	GafferOSL.OSLObject,

	"description",
	"""
	Executes OSL shaders to perform object processing. Use the shaders from
	the OSL/ObjectProcessing menu to read primitive variables from the input
	object and then write primitive variables back to it.
	""",

	plugs = {

		"shader" : [

			"description",
			"""
			The shader to be executed - connect the output from an OSL network here.
			A minimal shader network to process P would look like this :

				InPoint->ProcessingNodes->OutPoint->OutObject
			""",

			"nodule:type", "GafferUI::StandardNodule",
			"noduleLayout:section", "left",

		],
		"interpolation" : [

			"description",
			"""
			Interpolation mode in which to process the object. 
			All primitive variables are resampled to match the selected interpolation. 
			""",

			"preset:Uniform", IECore.PrimitiveVariable.Interpolation.Uniform,
			"preset:Vertex", IECore.PrimitiveVariable.Interpolation.Vertex,
			"preset:FaceVarying", IECore.PrimitiveVariable.Interpolation.FaceVarying,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		]

	}

)

